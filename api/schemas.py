from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str
    products_name: List[str]
    status: str
    role_ids: List[int]
    abilities: dict
    exp: datetime
    sub: Optional[int]
