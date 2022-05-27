from datetime import datetime
from typing import List, Optional, Union

from pydantic import BaseModel


class AgreementsItem(BaseModel):
    id: int
    ord: int
    label_pl: str
    code: str
    agreement_full_text_pl: str
    is_active: bool
    is_required: bool
    is_valid_from: datetime
    is_valid_to: datetime
    created_at: datetime
    fk_dict_application_id: int
    version_id: int
    extra_data: Optional[dict]

    class Config:
        orm_mode = True


class AgreementsResponse(BaseModel):
    status: int = 200
    data: List[AgreementsItem]


class DataProcessingPurposeItem(BaseModel):
    id: int
    label_pl: str
    code: str
    is_related_to_data_collection: bool
    is_related_to_data_processing: bool

    class Config:
        orm_mode = True


class DataProcessingPurposeResponse(BaseModel):
    status: int = 200
    data: List[DataProcessingPurposeItem]


class UserDataType(BaseModel):
    id: int
    user_data_meta_name: str
    user_data_label_pl: str
    is_validated: bool
    validation_formula: Optional[str] = None
    data_standard_description: Optional[str] = None
    is_unique: bool
    is_filtrable: bool
    is_displayed_by_admin: bool
    is_displayed_by_user: bool
    is_anonymous: bool
    is_retention_subject: bool
    admin_order: int

    class Config:
        orm_mode = True


class UserDataTypeResponse(BaseModel):
    status: int = 200
    data: List[UserDataType]


class Filter(BaseModel):
    id: int
    user_data_meta_name: str
    user_data_label_pl: str
    data_standard_description: Optional[str] = None
    admin_order: int
    data_values: Union[List, None]

    class Config:
        orm_mode = True


class FiltersResponse(BaseModel):
    status: int = 200
    data: List[Filter]


class UserTypeItem(BaseModel):
    id: int
    label_pl: Optional[str] = None
    code: str

    class Config:
        orm_mode = True


class UserTypeResponse(BaseModel):
    status: int = 200
    data: List[UserTypeItem]


class Country(BaseModel):
    id: int
    lang: str
    code: str
    name: str

    class Config:
        orm_mode = True


class CountryResponse(BaseModel):
    status: int = 200
    data: List[Country]


class Voivodeship(BaseModel):
    id: int
    lang: str
    code: str
    name: str

    class Config:
        orm_mode = True


class VoivodeshipResponse(BaseModel):
    status: int = 200
    data: List[Voivodeship]


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenAbilities(BaseModel):
    auth: Optional[dict]
    brisk: Optional[dict]
    umpire: Optional[dict]
    wicket: Optional[dict]


class TokenClient(BaseModel):
    id: int
    name: str
    language: str


class TokenPayload(BaseModel):
    id: int
    full_name: str
    email: str
    abilities: TokenAbilities
    client: TokenClient
    exp: datetime

