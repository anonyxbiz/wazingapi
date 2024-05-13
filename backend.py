# backend.py
from algo.initialize import*
from algo.apps import Components, Discord, Pages
from ai import Wazingai
      
class Backend_apps:
    def __init__(self):
        self.comps = Components()
        self.set_headers = Pages()
        self.wazingai = Wazingai()
        
    async def incoming(self, request):
        try:
            if request.method == "GET":
                return request.query
                    
            elif request.method == "POST": 
                return await self.comps.get_json(request)
        except Exception as e:
            await Discord().logger(f'Application log: {e}')
    
    async def dealer(self, request, response):
        await self.set_headers.verify_request(request, response, do='headers only')
        try:
            req_data = await self.incoming(request)   
            if req_data:
                model = req_data["model"] 
                query = req_data["query"]
                ip = request.remote_addr
                  
                if model == 'ai':
                    detail = await self.wazingai.aidata(query, ip)
                else:
                    detail = query
                
                data = detail
            else:
                abort(403, "Something wen't wrong processing your request")
                
        except Exception as e:
            await Discord().logger(f'Application log: {e}')
            abort(403, f"Something wen't wrong on our end {e}")
        return data
        
if __name__ == '__main__':
    pass