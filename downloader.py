# downloader.py
from initialize import*
from apps import Youtube_gate, Discord

yt = Youtube_gate()

class Downloader:
    token = 'YLMdxoWguPEUrBlYyfnwg8kHptqrUxxM7e0H3RrjKQGe6RcHuuSxmcLhl310yaFt'
    cookies = {
            'csrftoken': token,
        }
    headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.tubeninja.net',
            'Referer': 'https://www.tubeninja.net/welcome?url=https%3A%2F%2Fyoutu.be%2Fxidw5eulpOM%3Fsi%3DgYQ25K8JXu4kPUYJ',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
        }
        
    def __init__(self):
        pass
        
    async def scrape_dl(self, url):
        data = {
            'url': url,
            'csrfmiddlewaretoken': self.token,
        }
        
        r = rqs.post('https://www.tubeninja.net/get', cookies=self.cookies, headers=self.headers, data=data)
        
        if r.status_code == 200:
            html = bs4(r.text, "html.parser")
            image = html.find_all("img")[0]['src']
            content = html.find_all("a")
            
        return content, image 
    
    async def get_dl(self, url, format_):
        try:
            dls, img = await self.scrape_dl(url)
            if dls:
                for v in dls:
                    href = v.attrs['href']
                    if not href.startswith('https://www.4kdownload.com'):
                        video_meta = await yt.video_data(url)
                        
                        res_data = {"url": href}
                        
                        res_data.update(video_meta)
                        return res_data
            else:
                return False
                          
        except Exception as e:
            await Discord().logger('Application exception: {}'.format(e))
            return False
            
if __name__=="__main__":
    dl = Downloader()
    p(a.run(dl.get_dl('https://m.youtube.com/watch?v=ypPSrRYOAj4', 'mp4')))
    