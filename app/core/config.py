from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    """Settings class with a list of variables used in the application."""

    app_title: str = 'QRKot application'
    app_description: str = 'Application for the Cat Charitable Foundation'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = 'FIRST_SUPERUSER_EMAIL'
    first_superuser_password: Optional[str] = 'FIRST_SUPERUSER_PASSWORD'
    type: Optional[str] = 'type'
    project_id: Optional[str] = 'project_id'
    private_key_id: Optional[str] = 'private_key_id'
    private_key: Optional[str] = 'private_key'
    client_email: Optional[str] = 'client_email'
    client_id: Optional[str] = 'client_id'
    auth_uri: Optional[str] = 'auth_uri'
    token_uri: Optional[str] = 'token_uri'
    auth_provider_x509_cert_url: Optional[str] = 'auth_provider_x509_cert_url'
    client_x509_cert_url: Optional[str] = 'client_x509_cert_url'
    email: Optional[str] = 'email'

    class Config:
        env_file = '.env'


settings = Settings()
