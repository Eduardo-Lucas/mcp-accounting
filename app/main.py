from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="MCP Accounting Server",
    version="0.1"
)

app.include_router(router)


@app.get("/health")
def health():

    return {"status": "ok"}
