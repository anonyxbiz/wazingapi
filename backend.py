# backend.py
from algo.initialize import*
from algo.apps import Components, Discord, Pages
from ai import Wikipedia, Wazingai

class Analytics:
    def __init__(self):
        self.queries = [{'ip': '192.160.100.1', 'queries': [{"detail": {"query": 'query', "output": 'reply', "combined": 'chat'}}]}]
                
    async def user_queries(self, ip, query):
        user_data = None
        for i in self.queries:
            if ip == i['ip']:
                i['queries'][0]['detail']['combined'] += query['detail']['combined']
                user_data = i
                break
            
        if user_data == None:
            user_data = {'ip': ip, 'queries': [query]}
            self.queries.append(user_data)

        return user_data

    async def user_chats(self, ip):
        for i in self.queries:
            if ip == i['ip']:
                user_data = i
                return user_data 
        return False
        
class Backend_apps:
    def __init__(self):
        self.comps = Components()
        self.set_headers = Pages()
        self.wikipedia = Wikipedia()
        self.wazingai = Wazingai()
        self.analytics = Analytics()
        
    async def incoming(self, request):
        if request.method == "GET":
            return request.query
                
        elif request.method == "POST": 
            return await self.comps.get_json(request)
    
    async def wikidata(self, content):
        return await self.wikipedia.wiki(content)

    async def aidata(self, content, request):
        all_chats = await self.analytics.user_chats(request.remote_addr)
        if all_chats:
            content = all_chats['queries'][0]['detail']['combined']+= f'Me: {query}\nYou: '
        else:
            content = f'Me: {query}\nYou: '
            
        reply = await self.wazingai.chat(content)
        
        if reply:
            chat = f'Me: {query}\nYou: {reply}\n'
            
        detail = {"detail": {"query": query, "output": reply, "combined": chat}}

        data = await self.analytics.user_queries(request.remote_addr, detail)
        
        return data

        
    async def dealer(self, request, response):
        try:
            req_data = await self.incoming(request)   
            if req_data:
                model = req_data["model"] 
                query = req_data["query"]
                
                if model == 'ai':
                    detail = await self.aidata(query, request)
                else:
                    detail = query
                
                data = detail
              
            else:
                abort(403, "Something wen't wrong processing your request")
                
        except Exception as e:
            await Discord().logger(f'Application log: {e}')
            abort(403, f"Something wen't wrong on our end {e}")
        await self.set_headers.verify_request(request, response, do='headers only')
        return data
        
if __name__ == '__main__':
    pass
