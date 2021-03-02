import redis
import time
import secrets
import requests
from flask import Flask
app = Flask(__name__)

runningCount = 2
client = redis.Redis(host='myredis', port=6379, db=0)
reqSet = "requestSet"

@app.route('/call/')
def call_long():
    hashkey = secrets.token_hex(nbytes=16)

    print(f"[{hashkey}][begin] there are {client.scard(reqSet)} tasks in queue...")
    while client.scard(reqSet) > runningCount:
        print(f"[{hashkey}] waitting...")
        time.sleep(3) #sleep 3 seconds

    client.sadd(reqSet, hashkey)
    response = requests.get('http://app:5000/long/').content
    client.srem(reqSet, hashkey)
    print(f"[{hashkey}][end]")

    return response

if __name__ == '__main__':
    app.run('0.0.0.0', 5050, threaded=True)




