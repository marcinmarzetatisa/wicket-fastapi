import os

from fastapi import Depends, FastAPI

from mangum import Mangum

from api.dependencies import has_access
from api.endpoints import crypto, hello

stage = os.environ.get('STAGE', None)
openapi_prefix = f"/{stage}" if stage else "/"

app = FastAPI(title="Wicket FastAPI", openapi_prefix=openapi_prefix)

PROTECTED = [Depends(has_access)]

app.include_router(crypto.router, tags=["crypto"])
app.include_router(hello.router, tags=["token"], dependencies=PROTECTED)


@app.get("/")
async def root():
    return {"message": "Hello World"}


handler = Mangum(app=app)
