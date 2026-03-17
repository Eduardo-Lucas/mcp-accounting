from fastapi import FastAPI
from app.api.routes import router

from app.core.database import Base, engine
from app.models.transaction import Transaction

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MCP Accounting Server",
    version="0.1"
)

app.include_router(router)


@app.get("/health")
def health():

    return {"status": "ok"}
