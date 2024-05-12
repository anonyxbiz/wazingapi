# backend.py
from algo.initialize import*
from algo.apps import Components, Discord, Pages
#from algo.traffic import Analytics
from ai import Wikipedia, Wazingai

class Backend_apps:
    def __init__(self):
        self.comps = Components()
        self.set_headers = Pages()
        self.wikipedia = Wikipedia()
        self.wazingai = Wazingai()
        self.queries = [{'ip': '192.160.100.1', 'queries': []}]
        
    async def analytics(self, ip, query):
        self.user = None
        for i in self.queries:
            if ip == i['ip']:
                self.user = i
                break
            
        if self.user == None:
            self.user = {'ip': ip, 'queries': []}
        
        self.user['queries'].append(query)
        return self.user
        
    async def incoming(self, request):
        if request.method == "GET":
            return request.query
                
        elif request.method == "POST": 
            return await self.comps.get_json(request)
    
    async def wikidata(self, content):
        return await self.wikipedia.wiki(content)

    async def aidata(self, content):
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
                    reply = await self.aidata(query)
                else:
                    reply = query
                
                detail = {"detail": {"query": query, "output": reply}}
                
                data = await self.analytics.(request.remote_addr, detail)
              
            else:
                abort(403, "Something wen't wrong processing your request")
                
        except Exception as e:
            await Discord().logger(f'Application log: {e}')
            abort(403, f"Something wen't wrong on our end {e}")
        await self.set_headers.verify_request(request, response, do='headers only')
        return data
        
if __name__ == '__main__':
    pass
