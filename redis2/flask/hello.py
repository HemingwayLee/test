import redis
from flask import Flask
app = Flask(__name__)

r = redis.Redis(host='myredis', port=6379, db=0)

@app.route('/')
def hello_world():
    return 'Hello, World 2'

@app.route('/set/')
def set_foo():
    r.set('foo', 'bar')
    return 'ok'

@app.route('/get/')
def get_foo():
    return f"The foo is {r.get('foo')}"

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)

