import os
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import quote_plus

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)
class Settings:
    PROJECT_TITLE: str = "JobBoard"
    PROJECT_VERSION: str = "1.0.1"
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:%s@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}" % quote_plus(POSTGRES_PASSWORD)

settings = Settings()    