# apps.py
from initialize import*

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)  # Connect to SQLite database
        self.cursor = self.conn.cursor()
        a.run(self.create_table()) # Create a table if it doesn't exist
    
    async def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS items
                               (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, value INTEGER)''')
        self.conn.commit()  # Commit changes to the database
    
    async def add_item(self, name, data):
        self.cursor.execute('''INSERT OR REPLACE INTO items (name, value) VALUES (?, ?)''', (name, data))
        self.conn.commit()
        return self.cursor.lastrowid    
        
    async def check_item(self, name):
        check = self.cursor.execute('''SELECT * FROM items WHERE name=?''', (name,))
        complete = self.cursor.fetchone()
        
        if complete:
            return j.loads(complete[2])
        else:
            return None
         
    async def update_item(self, name, new_value):
        self.cursor.execute('''UPDATE items SET value=? WHERE name=?''', (new_value, name))
        self.conn.commit()
        return self.cursor.rowcount
    async def delete_item(self, name):
        self.cursor.execute('''DELETE FROM items WHERE name=?''', (name,))
        self.conn.commit()
        return self.cursor.rowcount
      
class Pages:
    def __init__(s):
        s.app = Components()
        s.protect = Protect()
        
    async def page_manager(s, page, request, response):
        ip = request.remote_addr
        set_res = await s.response_config(request, response)
        
        if not set_res:
            msg = 'You"re not supposed to be here'
            await Discord().logger('Request Aborted from IP: {}, Error message: {}'.format(ip, msg))
            abort(403, msg)
                
        if os.path.isfile(f'static/page/{page}.html'):
            page_content = {'token': set_res, 'views': 'views'}
            return template(f'static/page/{page}.html', page_content=page_content)
            
        else:
            msg = "The page you're looking for cannot be found"
            await Discord().logger('Request Aborted from IP: {}, Error message: {}'.format(ip, msg))
            
            abort(404, msg)
            
    async def response_config(s, request, response):
        verification = await s.verify_request(request, response, do='all')
        
        return verification
    
    async def verify_request(s, request, response, do):
        host = await s.app.get_header(request, 'Host')
        try:
            if do == 'all':
                ip = request.remote_addr
                token = await s.protect.tokenize(ip)
                
            response.set_header('strict-transport-security', 'max-age=63072000; includeSubdomains')
            response.set_header('x-frame-options', 'SAMEORIGIN')
            response.set_header('x-xss-protection', '1; mode=block')
            response.set_header('x-content-type-options', 'nosniff')
            response.set_header('referrer-policy', 'origin-when-cross-origin')
            response.set_header('server', 'Secure')
            
            if do == 'all':
                return token
            else:
                return response
        except Exception as e:
            await Discord().logger('Request Aborted from IP: {}, Error message: {}'.format(ip, e))
            abort(406, e)            
    
class Components:
    def __init__(s):
        s.fer_key = 'UKP89oA1T_01-jcheufpv9Y3JaeX1Se03n1u7Qq9gjY='
        s.allowed_origins = {'tonka.wazing.site', 'devops.wazing.site'}

    async def encrypt(s, parent):
        try:
            cipher_suite = Fernet(s.fer_key)
            encrypted_bytes = cipher_suite.encrypt(parent.encode())
            token = base64.urlsafe_b64encode(encrypted_bytes).rstrip(b'=').decode()
            return token
        except Exception as e:
            await Discord().logger(f'Application log: {e}')
            return False
            
    async def decrypt(s, token):
        try:
            padded_token = token + '=' * (-len(token) % 4)
            encrypted_bytes = base64.urlsafe_b64decode(padded_token.encode())
            cipher_suite = Fernet(s.fer_key)
            decrypted_bytes = cipher_suite.decrypt(encrypted_bytes)
            decrypted_data = decrypted_bytes.decode()
            return decrypted_data
        except Exception as e:
            await Discord().logger(f'Application log: {e}')
            return False
               
    async def get_json(s, r):    
        return j.loads(r.body.getvalue().decode('utf-8'))          
        
    async def get_header(s, request, value):    
        return request.get_header(value)

class Protect:
    def __init__(self):
        self.comps = Components()
        self.db = Database('twizzy.db')
        
    async def tokenize(self, ip):
        is_valid_identify = await self.db.check_item(ip)
        
        if is_valid_identify is not None:
            return is_valid_identify['token']
        
        gen_time = str(dt.now().time()) 
        token = await self.comps.encrypt('wazing'+gen_time)
        
        identity = {'ip': ip, 'token': token, 'gen_time': gen_time}
         
        update_db = await self.db.add_item(ip, j.dumps(identity))
        return token
    
    async def validation(self, request, token, response):
        ip = request.remote_addr
        
        is_valid_identify = await self.db.check_item(ip)
        
        if is_valid_identify is not None:
            if token == is_valid_identify['token']:
                return is_valid_identify['token']
                
            return False
        else:
            abort(406, "An error occured during validation")
             
    async def middleware(self, request, response):
        token = await self.comps.get_header(request,'validation')
        
        if token:
            verify = await self.validation(request, token, response)

            if not verify:
                abort(406, 'Invalid Token')
                
        else:
            abort(406, 'Token is missing')
            
        return 'valid'

def keepmealive(url, other):
    # Get the site to keep it active
    quits = 0
    gets = 0
    try:
        while quits <= 1:
            sleep(30)
            rqs.get(url)
            gets += 1
            
    except KeyboardInterrupt:
        quits += 1
        p('Keepalive Stopping...')
    except Exception as e:
        a.run(Discord().logger(f'Application log: {e}'))

class Discord:
    def __init__(self):
        self.server_name = 'webalgo.onrender.com'
    async def logger(self, msg):
        msg = self.server_name +': '+ str(msg)
        
        webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/1236829940616396800/Ryf1pDw9nP7kwezqdGNHlNaCcfqCpIxQwSbMiJQ3chEvlp2DF1Zkdjcfg1TFMU2ZQeHO")
        
        if webhook.send(content=msg):
            return True

class Obsfucation:
    def __init__(self):
        pass
    
    async def obsfucate_code(self, file):
        try:
            with open(f'./static/js/{file}', 'r') as f:
                raw = f.read()
            
                json_data = {
                    'code': raw,
                }
                
                r = rqs.post('https://javascript-obfuscator.onrender.com/api/obsfucation', headers={'validation': 'mzing'}, json=json_data)
                
                data = r.text
            with open(f'./static/js/{file}', 'w') as f:
                f.write(data)  
                         
                return True
        except Exception as e:
            await Discord().logger(f'Application log: {e}')

class Youtube_gate:
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

class Test:
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
                        
if __name__ == '__main__':
    pass