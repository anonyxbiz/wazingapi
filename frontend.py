# frontend.py
from initialize import*
from apps import Components, Protect, Discord
from downloader import Downloader

app = Components()
protect = Protect()
dl = Downloader()

class Dl_app:
    def __init__(self):
        pass
        
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
