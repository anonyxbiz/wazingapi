# apps.py
from algo.initialize import*
from traffic import Analytics

class Pages:
    def __init__(s):
        s.app = Components()
        s.analytics = Analytics()
        
    async def page_manager(s, page, request, response):
        ip = request.remote_addr
        await s.analytics.check(ip)
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
                token = "test"
                
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

if __name__ == '__main__':
    pass