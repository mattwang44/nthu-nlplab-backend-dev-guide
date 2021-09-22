import os

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import redis

app = FastAPI()
redis_client = redis.Redis(os.environ.get('REDIS_HOST'))
redis_client.set("count", 0)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:8080",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/counter")
def get_count():
    count = redis_client.get("count")
    if not count:
        redis_client.set("count", 0)
        count = 0
    return {"count": count}

@app.post("/counter")
async def increment_by(request: Request):
    body = await request.json()
    num = int(body.get('num', 0))
    count = redis_client.incrby("count", num)
    return {"count": count}

