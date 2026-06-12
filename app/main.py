from fastapi import FastAPI
from routes import router  # app.routes yerine routes

app = FastAPI(title="User Service")

app.include_router(router, prefix="/users")

@app.get("/health")
def health():
    return {"status": "ok"}
