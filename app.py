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

if __name__ == "__main__":
    app.run(debug=True)