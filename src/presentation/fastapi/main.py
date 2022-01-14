from fastapi import FastAPI
from .routes.router import router

def get_app():
    app = FastAPI()

    app.include_router(router)

    return app
