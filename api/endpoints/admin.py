from fastapi import APIRouter, Depends

from api import schemas
from api.dependencies import has_access

router = APIRouter(prefix="/admin", tags=["admin"], dependencies=[Depends(has_access)])


@router.get("/hello/")
async def say_hi(token: dict = Depends(has_access)):
    token_payload = schemas.TokenPayload(**token)

    return {
        "message": f"Hi {token_payload.first_name}!",
        "token_payload": token_payload
    }
