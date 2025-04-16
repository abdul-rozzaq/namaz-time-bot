from fastapi import FastAPI, Request
from src.core.lifespan import lifespan
from src.controllers.webhook import router as webhook_router

app = FastAPI(lifespan=lifespan)

app.include_router(webhook_router, prefix="/telegram-webhook")


@app.get("/")
def root():
    return {"status": "ok"}
