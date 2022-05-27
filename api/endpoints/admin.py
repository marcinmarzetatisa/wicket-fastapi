from fastapi import APIRouter, Depends, Security

from api import schemas
from api.dependencies import has_access
from api.schemas import TokenAbilities, TokenPayload

AUTH_TOKEN = Security(has_access)

router = APIRouter(prefix="/admin", tags=["admin"], dependencies=[AUTH_TOKEN])


# @router.get("/hello")
# def say_hi(token: dict = AUTH_TOKEN):
#     token_payload = schemas.TokenPayload(**token)
#
#     response = {
#         "message": f"Hi {token_payload.full_name}!",
#         "auth_user_id": token_payload.id,
#         "auth_user_full_name": token_payload.full_name,
#         "auth_user_email": token_payload.email,
#         "token_expires": token_payload.exp,
#         "token_abilities": token_payload.abilities,
#         "client_id": token_payload.client.id,
#         "client_name": token_payload.client.name,
#         "client_language": token_payload.client.language,
#     }
#
#     return response


@router.get("/abilities/wicket")
def get_wicket_permissions(abilities: dict = AUTH_TOKEN):
    return "Access granted"


@router.get("/abilities/auth")
def get_auth_permissions(abilities: dict = AUTH_TOKEN):
    return abilities.get("auth", {})
