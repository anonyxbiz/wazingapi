# frontend.py
from initialize import*
from apps import Components, Discord, Pages
from algo.traffic import Analytics

class Dl_app:
    def __init__(self):
        self.analytics = Analytics()
        self.comps = Components()
        self.set_headers = Pages()
   
    async def dler(self, request, response):
        try:
            if request.method == "GET":
                incoming = request.query
                
            elif request.method == "POST": 
                incoming = self.comps.get_json(request)
                
            if incoming:
                link = incoming["link"] or "None"
                test = incoming["test"] or "None"
                
                data = {"detail": [{"link": link, "test": test}]}
                
                visits = await self.analytics.check(request.remote_addr)
                data.update(visits)
                
            else:
                abort(403, "Something wen't wrong processing the request")
        except Exception as e:
            await Discord().logger(f'Application log: {e}')
            abort(403, f"Something wen't wrong on our end {e}")
     
        await self.set_headers.verify_request(request, response, do='headers only')
        return data
        
if __name__ == '__main__':
    pass
