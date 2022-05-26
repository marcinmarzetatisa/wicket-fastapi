from pydantic import BaseSettings


class Settings(BaseSettings):
    public_key: str
    sqlalchemy_url: str
    access_token_expire_minutes: int = 60 * 24 * 8
    super_user_email: str = "admin@example.com"
    super_user_password: str = None

    class Config:
        env_file = ".env"


settings = Settings()
