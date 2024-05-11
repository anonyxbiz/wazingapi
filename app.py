# app.py
from initialize import*
from frontend import Dl_app
from apps import Pages, Discord

app = Bottle()
pages = Pages()
logman = Discord()
testing = Dl_app()

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

@app.route('api/v1/test', method=['GET', 'POST'])
def test():
    a.run(pages.verify_request(request, r, do='headers_only'))
    
    return a.run(testing.dler(request, r))
    
@app.route('/<page>')
def controlla(page):
    webpage = a.run(pages.page_manager(page, request, r))
    
    return webpage
        
if __name__=="__main__":
    if not args.thread:
        from apps import keepmealive
        url = app_info['url']
        task_thread = Thread(target=keepmealive, args=(url, url))
        
        task_thread.start()
        
    run(app=app, host="0.0.0.0", port="8004", debug=True, reloader=True)
    