from typing import List, ClassVar
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base 
from firebase_admin import credentials
import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Acessar a variável de ambiente DB_URL
db_url = os.getenv("DB_URL")
print(db_url)
service_account_key_path = os.getenv("SERVICE_ACCOUNT_KEY_PATH")

# Criar as credenciais a partir do arquivo serviceAccountKey.json
cred = credentials.Certificate(service_account_key_path)

Base = declarative_base()

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "OTICA-HOPE"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    DATABASE_URL: str=db_url
    FIREBASE_CREDENTIALS: credentials.Certificate = cred
    DBBaseModel: ClassVar = Base

    class Config:
        case_sensitive = True

ConfigSetting = Settings()        