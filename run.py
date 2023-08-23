#from flask import Flask
# app = Flask(__name__)
 
# @app.route('/')
# def hello_world():
#     return '<html><body><h1>sample</h1></body></html>'
 
# if __name__ == '__main__':
#     app.run()


from flask import Flask
from flask import render_template
 
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    values = {"val1": 100, "val2" :200}
    return render_template('index.html', values=values)
 
if __name__ == '__main__':
    app.run()

