# app.py
from algo.initialize import*
from algo.apps import Pages, Discord, keepmealive
from backend import Backend_apps

app = Bottle()
pages = Pages()
logman = Discord()
backend = Backend_apps()

@app.route('/static/<filename:path>')
def static(filename):
    good_files = ['css/style.css', 'js/script.js', 'images/favicon.png']
    if filename == 'js/script.js':
        abort(404, 'Not found')
        
    try:
        return static_file(filename, root='./static')
    except Exception as e:
        a.run(Discord().logger(f'Application log: {e}'))
        abort(403, e)

@app.route('/')
def index():
    try:
        webpage = a.run(pages.page_manager('index', request, r))
    except Exception as e:
        a.run(Discord().logger(f'Application log: {e}'))
    return webpage
    
@app.route('/<page>')
def controlla(page):
    try:
        webpage = a.run(pages.page_manager(page, request, r))
    
        return webpage
    except Exception as e:
        abort(403, e)
        a.run(Discord().logger(f'Application log: {e}'))
 
@app.route('/api/v1/models', method=['GET','POST'])
def models():
    try:
        data = a.run(backend.dealer(request, r))
        return data
    except Exception as e:
        abort(403, e)
        a.run(logman.logger(e))
       
if __name__=="__main__":
    stay = False
    if stay:
        url = app_info['url']
        task_thread = Thread(target=keepmealive, args=(url, url))
        task_thread.start()
    
    run(app=app, host="0.0.0.0", port="8004", debug=True, reloader=True)
    
    