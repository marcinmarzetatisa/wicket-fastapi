from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api import crud, schemas
from api.dependencies import get_db

router = APIRouter(
    prefix="/dictionaries",
    tags=["dictionaries"],
)


@router.get("/countries/")
def get_countries(db: Session = Depends(get_db)):
    """Get list of countries"""

    countries = crud.get_countries(db)
    return schemas.CountryResponse(data=countries)


@router.get("/voivodeships/")
def get_voivodeships(db: Session = Depends(get_db)):
    """Get list of voivodeships"""

    voivodeships = crud.get_voivodeships(db)
    return schemas.VoivodeshipResponse(data=voivodeships)
