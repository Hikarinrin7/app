from flask import Flask, render_template

app = Flask(__name__)

#ルート / に来たときにindex.htmlを読み込む
@app.route('/')
def index():
    return render_template('index.html')

#ルート /send に来たときにsend.htmlを読み込む
@app.route('/send')
def send():
    return render_template('send.html')

#ルート /sendperson に来たときにsendperson.htmlを読み込む
@app.route('/sendperson')
def sendperson():
    return render_template('sendperson.html')

#ルート /sendperson に来たときにsendperson.htmlを読み込む
@app.route('/complete')
def complete():
    return render_template('complete.html')

if __name__ == "__main__":
    app.run(debug=True)