from fastapi import FastAPI, HTTPException
import redis

app = FastAPI()
r = redis.Redis(host="redis-service", port=6379, decode_responses=True)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with Redis"}

@app.get("/increment/{key}/{amount}")
def increment_key(key: str, amount: int):
    if not r.exists(key):
        r.set(key, 0)
    try:
        new_value = r.incrby(key, amount)
        return {"key": key, "new_value": new_value}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
