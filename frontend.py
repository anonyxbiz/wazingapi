# frontend.py
from initialize import*
from apps import Components, Discord
from test import Test

class Dl_app:
    def __init__(self):
        self.test = Test()
        self.comps = Components()
   
    async def dler(self, request, response):
        try:
            link = request.query.link
            if not link:
                incoming = self.comps.get_json(request )
                link = incoming['link']
            
            visits = self.test.check(request.remote_addr)
            
            data = {"detail": link}
            data.update(visits)
        except Exception as e:
            p(e)
            await Discord().logger(f'Application log: {e}')
                
        return data
        
if __name__ == '__main__':
    pass
