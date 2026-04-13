import redis
from flask import Flask

app = Flask(__name__)

r = redis.Redis(host='cache_db', port=6379, decode_responses=True)

@app.route('/')
def hello():
    r.incr('contador')
    return f"Visitas: {r.get('contador')}"

app.run(host='0.0.0.0', port=5000)