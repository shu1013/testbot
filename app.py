#ここから第四章
from flask import Flask

app = Flask(__name__)

@app.route('/testbot')
def hello_world():
    return print('Hello_World!!')

if __name__ == '__main__':
    app.run()
