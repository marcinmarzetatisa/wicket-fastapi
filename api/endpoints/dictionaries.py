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


@router.get("/user_data_types/")
def get_user_data_types(db: Session = Depends(get_db)):
    """Get list of user data types"""

    user_data_types = crud.get_user_data_types(db)
    return schemas.UserDataTypeResponse(data=user_data_types)


@router.get("/filters/")
def get_audience_filters(db: Session = Depends(get_db)):
    """Get ordered list of newsletter audience filters"""

    filters = crud.get_user_data_types_with_standard_description(db)
    for f in filters:
        if (
            f.data_standard_description == "enum"
            and f.user_data_meta_name == "country"
        ):
            f.data_values = [v[0] for v in crud.get_distinct_data_values_country(f.id, db)]
        elif (
            f.data_standard_description == "enum"
            and f.user_data_meta_name == "voivodeship"
        ):
            f.data_values = [v[0] for v in crud.get_distinct_data_values_voivodeship(f.id, db)]
        elif f.data_standard_description == "enum":
            f.data_values = [v[0] for v in crud.get_distinct_data_values(f.id, db)]
        else:
            f.data_values = None

    return schemas.FiltersResponse(data=filters)


# @router.get("/user_list/")
# def get_filters(user_data_meta_name: str, db: Session = Depends(get_db)):
#     """Get list of filters"""
#
#     objects = crud.user_list_distinct_values_by_data_meta_name(
#         db,
#         user_data_meta_name=user_data_meta_name,
#     )
#     values = [o["data_value"] for o in objects]
#
#     return values
#
#
# @router.get("/enum_values/")
# def get_filter_values(data_type_id: int, db: Session = Depends(get_db)):
#     """Get list of filter values"""
#
#     objects = crud.user_list_distinct_enums(data_type_id, db)
#     values = [o["data_value"] for o in objects]
#
#     return values
