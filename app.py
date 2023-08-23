from flask import Flask, render_template # 追加

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') # 変更

@app.route('/send')
def send():
    return render_template('send.html')

if __name__ == "__main__":
    app.run(debug=True)