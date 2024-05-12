# frontend.py
from algo.initialize import*
from algo.apps import Components, Discord, Pages
from algo.traffic import Analytics
from ai import Wikipedia

class Dl_app:
    def __init__(self):
        self.analytics = Analytics()
        self.comps = Components()
        self.set_headers = Pages()
        self.wikipedia = Wikipedia()
   
    async def incoming(self, request):
        if request.method == "GET":
            incoming = request.query
                
        elif request.method == "POST": 
            incoming = await self.comps.get_json(request)
        return incoming
    
    async def wikidata(self, content):
        return await self.wikipedia.wiki(content)
        
    async def dler(self, request, response):
        try:
            req_data = await self.incoming(request)   
            if req_data:
                model = req_data["model"] 
                query = req_data["query"]
                
                if model == 'wiki':
                    reply = await self.wikidata(query)
                    
                else:
                    reply = query
                    
                data = {"detail": {"query": query, "output": reply}}
                
                visits = await self.analytics.check(request.remote_addr)
                
                data.update(visits)
            else:
                abort(403, "Something wen't wrong processing your request")
                
        except Exception as e:
            await Discord().logger(f'Application log: {e}')
            abort(403, f"Something wen't wrong on our end {e}")
        await self.set_headers.verify_request(request, response, do='headers only')
        return data
        
if __name__ == '__main__':
    pass
