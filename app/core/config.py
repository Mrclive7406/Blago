from typing import Optional

from pydantic import BaseSettings, EmailStr

SECRET = 'SECRET'
FOUNDATION_KYTTI = 'Кошачий благотворительный фонд'
DISCRIPTION_APP = 'Сервис для поддержки котиков!'
ENV = '.env'
DATABASE_URL = 'sqlite+aiosqlite:///./fastapi.db'


class Settings(BaseSettings):
    app_title: str
    app_description: str = DISCRIPTION_APP
    database_url: str = DATABASE_URL
    secret: str = SECRET
    first_superuser_email: Optional[EmailStr]
    first_superuser_password: Optional[str] = None
    # Переменные для Google API
    type: Optional[str] = None
    project_id: Optional[str] = None
    private_key_id: Optional[str] = None
    private_key: Optional[str] = None
    client_email: Optional[str] = None
    client_id: Optional[str] = None
    auth_uri: Optional[str] = None
    token_uri: Optional[str] = None
    auth_provider_x509_cert_url: Optional[str] = None
    client_x509_cert_url: Optional[str] = None
    email: Optional[str]

    class Config:
        env_file = ENV


settings = Settings()
