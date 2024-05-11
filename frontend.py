# frontend.py
from initialize import*
from apps import Components, Discord, Pages
from test import Test

class Dl_app:
    def __init__(self):
        self.test = Test()
        self.comps = Components()
        self.set_headers = Pages()
   
    async def dler(self, request, response):
        try:
            if request.method == "GET":
                incoming = dict(request.query.decode())
                
            elif request.method == "POST": 
                incoming = self.comps.get_json(request)
            if incoming:
                link = incoming["link"] or "None"
                test = incoming["test"] or "None"
                
                data = {"detail": [{"link": link, "test": test}]}
                
                async with self.test.check(request.remote_addr) as visits:
                    data.update(visits)
            else:
                abort(403, "Something wen't wrong on our end")
        except Exception as e:
            p(e)
            await Discord().logger(f'Application log: {e}')
            abort(403, "Something wen't wrong on our end")
     
        await self.set_headers.verify_request(request, response, do='headers only')
        return data
        
if __name__ == '__main__':
    pass
