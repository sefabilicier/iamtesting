from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="User Service")

app.include_router(router, prefix="/users")


@app.get("/health")
def health():
    return {"status": "ok"}