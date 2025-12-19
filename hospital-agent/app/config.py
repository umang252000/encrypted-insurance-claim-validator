import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SERVICE_NAME = "hospital-agent"
    ENV = os.getenv("ENV", "dev")
    CYBORGDB_ENDPOINT = os.getenv("CYBORGDB_ENDPOINT", "http://cyborgdb:8080")
    TENANT_ID = os.getenv("HOSPITAL_ID", "hospital-A")

settings = Settings()