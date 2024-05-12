# backend.py
from algo.initialize import*
from algo.apps import Components, Discord, Pages
from ai import Wikipedia, Wazingai

class Analytics:
    def __init__(self):
        self.queries = [{'ip': '192.160.100.1', 'queries': []}]
                
    async def user_queries(self, ip, query):
        for i in self.queries:
            if ip == i['ip']:
                user_data = i
                break
            
        if not user_data:
            user_data = {'ip': ip, 'queries': [query]}
            self.queries.append(user_data)

        return user_data

    async def user_chats(self, ip):
        for i in self.queries:
            if ip == i['ip']:
                user_data = i
                return  user_data 
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
        all_chats = await self.user_chats(request.remote_addr)
        if all_chats:
            content = all_chats['detail']['combined']
                
        return await self.wazingai.chat(content)
        
    async def dealer(self, request, response):
        try:
            req_data = await self.incoming(request)   
            if req_data:
                model = req_data["model"] 
                query = req_data["query"]
                
                if model == 'wiki':
                    reply = await self.wikidata(query)
                elif model == 'ai':
                    reply = await self.aidata(query, request)
                else:
                    reply = query
                
                this_chat = f'Me: {query}\nYou: {reply}\n'
                
                detail = {"detail": {"query": query, "output": reply, "combined": this_chat}}
                
                data = await self.analytics.user_queries(request.remote_addr, detail)
              
            else:
                abort(403, "Something wen't wrong processing your request")
                
        except Exception as e:
            await Discord().logger(f'Application log: {e}')
            abort(403, f"Something wen't wrong on our end {e}")
        await self.set_headers.verify_request(request, response, do='headers only')
        return data
        
if __name__ == '__main__':
    pass
