from typing import List

from sqlalchemy import distinct, func
from sqlalchemy.orm import Session

from . import models

# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()
#
#
# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()
#
#
# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()
#
#
# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
#
#
# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()
#
#
# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item


def get_countries(db: Session) -> List[models.Country]:
    return db.query(models.Country).all()


def get_voivodeships(db: Session) -> List[models.Region]:
    return db.query(models.Region).all()


def get_user_data_types(db: Session) -> List[models.UserDataType]:
    return db.query(models.UserDataType).all()


def get_user_data_types_with_standard_description(
    db: Session,
) -> List[models.UserDataType]:
    return (
        db.query(models.UserDataType)
        .where(models.UserDataType.data_standard_description != "")
        .order_by(models.UserDataType.admin_order)
        .all()
    )


def user_count_by_data_meta_name_and_value(
    db: Session,
    user_data_meta_name: str,
    data_value: str,
) -> int:
    query = (
        db.query(models.FanUserData.data_value)
        # .join(models.UserDataType)
        .where(
            # func.lower(FanUserData.data_value) == func.lower(data_value),
            models.UserDataType.user_data_meta_name
            == user_data_meta_name,
        )
    )
    query = query.with_entities(func.count(distinct(models.FanUserData.data_value)))
    item_count = query.scalar()
    return item_count


def user_count_distinct_by_data_meta_name(
    db: Session,
    user_data_meta_name: str,
) -> int:
    query = (
        db.query(models.FanUserData.data_value)
        # .join(models.UserDataType)
        .where(
            models.UserDataType.user_data_meta_name == user_data_meta_name,
        )
    )
    query = query.with_entities(func.count(distinct(models.FanUserData.data_value)))
    item_count = query.scalar()
    return item_count


def user_list_distinct_values_by_data_meta_name(
    db: Session,
    user_data_meta_name: str,
):
    query = (
        db.query(models.FanUserData.data_value)
        # .join(models.UserDataType)
        .where(
            models.UserDataType.user_data_meta_name == user_data_meta_name,
        )
    )
    query = query.distinct(models.FanUserData.data_value).all()
    return query


def get_distinct_data_values(data_type_id: int, db: Session) -> List[str]:
    return (
        db.query(models.FanUserData.data_value)
        .where(
            models.FanUserData.fk_dict_user_data_type_id == data_type_id,
        )
        .distinct(models.FanUserData.data_value)
        .all()
    )


def get_distinct_data_values_country(data_type_id: int, db: Session) -> List[str]:
    return (
        db.query(models.Country.name)
        .where(
            models.FanUserData.fk_dict_user_data_type_id == data_type_id,
            models.FanUserData.data_value == models.Country.code,
        )
        .distinct(models.FanUserData.data_value)
        .all()
    )


def get_distinct_data_values_voivodeship(data_type_id: int, db: Session) -> List[str]:
    return (
        db.query(models.Region.name)
        .where(
            models.FanUserData.fk_dict_user_data_type_id == data_type_id,
            models.FanUserData.data_value == models.Region.code,
        )
        .distinct(models.FanUserData.data_value)
        .all()
    )
