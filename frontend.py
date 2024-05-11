# frontend.py
from initialize import*
from apps import Components, Discord
from test import Test

class Dl_app:
    def __init__(self):
        self.protect = Protect()
        self.test = ()
   
    async def dler(self, request, response):
        try:
            ip = request.remote_addr
            incoming_data = await app.get_json(request)
            
            if incoming_data:
                link = incoming_data['link']
            else:
                link = request.query.link
            
            if link:
                data = {'detail': link}
            else:
                data = {'detail': 'hi'}
                
            return data
        except Exception as e:
            p(e)
            await Discord().logger(f'Application log: {e}')
                
    
if __name__ == '__main__':
    pass
