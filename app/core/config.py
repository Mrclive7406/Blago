from typing import Optional

from pydantic import BaseSettings, EmailStr

SECRET = 'SECRET'
"""
Константам тоже стоит добавлять докстринги с описанием
"""
DISCRIPTION_APP = 'Сервис для поддержки котиков!'
"""
Описание приложения, которое поддерживает котиков.
"""
DB_URL = 'sqlite+aiosqlite:///./charity_project_donation.db'
"""
URL для подключения к базе данных.
В данном случае используется SQLite с асинхронной библиотекой.
"""
ENV_ = '.env'
"""
Имя файла конфигурации, содержащего переменные среды.
"""


class Settings(BaseSettings):
    app_title: str = None
    app_description: str = DISCRIPTION_APP
    database_url: str = DB_URL
    secret: str = SECRET
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
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
        env_file = ENV_


settings = Settings()
