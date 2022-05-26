import os

from fastapi import FastAPI

from mangum import Mangum

from api.endpoints import admin, dictionaries

stage = os.environ.get('STAGE', None)
openapi_prefix = f"/{stage}" if stage else "/"

app = FastAPI(title="Wicket FastAPI", openapi_prefix=openapi_prefix)

app.include_router(admin.router)
app.include_router(dictionaries.router)

handler = Mangum(app=app)
