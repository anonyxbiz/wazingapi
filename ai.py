# ai.py
from algo.initialize import*

class Wazingai:
    GOOGLE_API_KEY="AIzaSyA2Wuzo0_4IkhY6SMzm0wpPU3N2OyU7Y3Y"
    genai.configure(api_key=GOOGLE_API_KEY)
    
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            p(m.name)
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    
    def __init__(ai):
        pass
        
    async def to_markdown(ai, text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

    async def chat(ai, text):
        prompt = f"Me: {text}\nYou: "
        try:
            r = ai.model.generate_content(prompt)
            if r:
                return r.text.replace("*", "")
        except Exception as e:
            p(e)
            return e
    
class Wikipedia:
    def __init__(self):
        pass
    
    async def wiki(self, keyword):
        self.full_article = ''
        cookies = {
        'GeoIP': 'KE:30:Nairobi:-1.28:36.82:v4',
        'enwikimwuser-sessionId': '5502b21ef9c20da1291a',
        'WMF-Last-Access': '13-Mar-2024',
        'WMF-Last-Access-Global': '13-Mar-2024',
        'NetworkProbeLimit': '0.001',
        'WMF-DP': '441,c04,765',}
        headers = {
        'authority': 'en.m.wikipedia.org',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'referer': 'https://en.m.wikipedia.org/w/index.php?fulltext=search&search=Eminem+American+rapper&title=Special%3ASearch&ns0=1',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
        params = {
        'action': 'opensearch',
        'format': 'json',
        'formatversion': '2',
        'search': keyword,
        'namespace': '0',
        'limit': '10',}
        try:
            self.data = rqs.get('https://en.m.wikipedia.org/w/api.php', params=params, cookies=cookies, headers=headers)
            
            if self.data.status_code == 200:
                url = self.data.json()[3][0]
                self.data = rqs.get(url, cookies=cookies, headers=headers, allow_redirects=True)
                
                self.r = self.data.text
                self.soup = bs4(self.r, 'html.parser')
                self.summary = self.soup.find_all("p")
                
                for a in self.summary:
                    a = a.text.strip()
                    if a !='\n':
                        self.full_article+=f'{a} '
            else:
                self.full_article = 'I don\'t know '+keyword+' yet.'
        except Exception as e:
            p(e)
    
        self.full_article = await self.rmp(self.full_article)
        
        return self.full_article

    async def rmp(self, text):
        pattern = r'\([^)]*\)|\[[^\]]*\]'
        stripped_text = sub(pattern, '', text).replace('  ', ' ').strip()
        
        return stripped_text
        
if __name__ == "__main__":
    m = Wazingai()
    content = 'what is the meaning of life'
    data = a.run(m.chat(content))
    p(data)



