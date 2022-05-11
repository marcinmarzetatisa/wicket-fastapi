from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JOSEError, jwt

from api.database import SessionLocal

security = HTTPBearer()


async def has_access(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Function that is used to validate the token in the case that it requires it
    """

    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            key="secret",
            options={
                "verify_signature": False,
                "verify_aud": False,
                "verify_iss": False,
            },
        )
    except JOSEError as e:
        raise HTTPException(status_code=401, detail=str(e))

    return payload


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
