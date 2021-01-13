from flask import *
app= Flask(__name__)

@app.route('/')
def hello():
    return "hellow world"

@app.route('/index')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run()