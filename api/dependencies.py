from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JOSEError, jwt

from api.settings import settings
from api.database import SessionLocal

security = HTTPBearer()


def has_access(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Function that is used to validate the token
    """

    token = credentials.credentials
    key = settings.public_key

    try:
        payload = jwt.decode(token, key)
        token_abilities = payload.get("abilities", {})
        # token_data = TokenData(scopes=token_scopes, username=username)
    except JOSEError as e:
        raise HTTPException(status_code=401, detail=str(e))

    return token_abilities


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
