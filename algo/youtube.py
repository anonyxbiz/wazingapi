from initialize import*

class YouTube_Gate:
    def __init__(self):
        pass
        
    async def get_id(self, url):
        if 'watch?v=' in url:
            url = url.split('watch?v=')[1]
            if '&' in url:
                url = url.split('&')[0]
        elif 'youtu.be/' in url:
            url = url.split('youtu.be/')[1]
            if '?' in url:
                url = url.split('?')[0]
        
        return url
        
    async def video_data(self, url):
        try:
            video_id = await self.get_id(url)
            request = youtube.videos().list(
                part="snippet,contentDetails",
                id=video_id
            )
            response = request.execute()
           
            data = {"title": response['items'][0]['snippet']['title'], "thumbnail": response['items'][0]['snippet']['thumbnails']['default']['url']}
            
            return data
                                    
        except Exception as e:
            await Discord().logger('Application exception: {}'.format(e))
            abort(500, 'Unexpected error')
