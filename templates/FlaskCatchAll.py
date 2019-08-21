from flask import Flask
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    xSubPath = path.split("/")
    return 'You want path: %s' % xSubPath

if __name__ == '__main__':
    app.run()

'''    
if __name__ == '__main__':  
     app.run(host='127.0.0.1', port=80, debug=True, ssl_context='adhoc')
'''
