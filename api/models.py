from typing import List

from sqlalchemy import ARRAY, Boolean, Column, DateTime, ForeignKey, Integer, String, Text, func, text
from sqlalchemy.orm import relationship

from .database import Base


class Country(Base):
    __tablename__ = "dict_country"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    lang = Column(String(2), nullable=False)
    code = Column(String(2), nullable=False)
    name = Column(String(255), nullable=False)


class DataOperationType(Base):
    __tablename__ = "dict_data_operation_type"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    label_pl = Column(String, nullable=False)
    code = Column(String(50), nullable=False)


class DeviceType(Base):
    __tablename__ = "dict_device_type"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    label_pl = Column(String, nullable=False)
    code = Column(String(50), nullable=False)


class ProviderName(Base):
    __tablename__ = "dict_provider_name"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    provider_name = Column(String(100), index=True, nullable=False)


class Region(Base):
    __tablename__ = "dict_region"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    lang = Column(String(2), nullable=False)
    code = Column(String(2), nullable=False)
    name = Column(String(255), nullable=False)


class RequestedEvent(Base):
    __tablename__ = "dict_user_requested_event"

    id = Column(Integer, primary_key=True, nullable=False)
    event_name = Column(String(50), unique=True)
    description = Column(String)


class UserDataType(Base):
    __tablename__ = "dict_user_data_type"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    user_data_meta_name = Column(String(150), nullable=False)
    user_data_label_pl = Column(String(150), nullable=False)
    is_validated = Column(Boolean, default=False, nullable=False)
    validation_formula = Column(Text)
    data_standard_description = Column(Text)
    is_unique = Column(Boolean, default=False, nullable=False)
    is_filtrable = Column(Boolean, default=False, nullable=False)
    is_displayed_by_admin = Column(Boolean, default=False, nullable=False)
    is_displayed_by_user = Column(Boolean, default=False, nullable=False)
    is_anonymous = Column(Boolean, default=False, nullable=False)
    is_retention_subject = Column(Boolean, default=False, nullable=False)
    admin_order = Column(Integer, default=1000, nullable=False)


class UserType(Base):
    __tablename__ = "dict_user_type"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    label_pl = Column(String)
    code = Column(String(50), nullable=False)


class FanUserData(Base):
    __tablename__ = "fan_user_data"

    id = Column(Integer, primary_key=True, nullable=False)
    fk_fan_id = Column(
        Integer, ForeignKey("fan_user.fan_id"), index=True, nullable=False
    )
    fk_dict_user_data_type_id = Column(
        Integer, ForeignKey(UserDataType.id), nullable=False
    )
    data_value = Column(String)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    data_type: UserDataType = relationship(UserDataType, backref="users", lazy="joined")


class User(Base):
    __tablename__ = "fan_user"

    fan_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    fan_sub = Column(String(50), unique=True, index=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    email_verified = Column(Boolean, default=False)
    status = Column(String(50))
    redirect_url = Column(Text)
    for_integration = Column(
        ARRAY(Integer), server_default=text("'{}'::integer[]")
    )
    fk_invitation_code = Column(
        Integer, ForeignKey("invitation.invitation_id")
    )

    data: List[FanUserData] = relationship(
        "FanUserData", backref="fk_fan", lazy="joined"
    )
