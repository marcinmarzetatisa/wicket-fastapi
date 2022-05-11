import os

from fastapi import FastAPI

from mangum import Mangum

from api.endpoints import admin, crypto, dictionaries

stage = os.environ.get('STAGE', None)
openapi_prefix = f"/{stage}" if stage else "/"

app = FastAPI(title="Wicket FastAPI", openapi_prefix=openapi_prefix)

app.include_router(admin.router)
app.include_router(dictionaries.router)
app.include_router(crypto.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


handler = Mangum(app=app)
