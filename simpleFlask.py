from flask import Flask

app = Flask(__name__)

# 테스트 기능
@app.route('/hello')
def hello_Flask():
    return 'Hello, Flask'

@app.route('/hi')
def hi_Flask():
    return 'Hi, Flask'

if __name__ == '__main__':
    app.run(
    host="0.0.0.0",
    port=7777,
    debug=True)