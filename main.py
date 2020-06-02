import uvicorn
from fastapi import FastAPI
from starlette.requests import Request

from src.api.router import api_router
from src.core import config
from src.database.base_class import Base
from src.database.session import Session, engine

app = FastAPI(redoc_url="/docs", docs_url="/docs2")

Base.metadata.create_all(bind=engine, checkfirst=True)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(api_router, prefix=config.API_STR)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = Session()
    response = await call_next(request)
    request.state.db.close()
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
