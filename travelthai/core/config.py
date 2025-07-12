from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SQLDB_URL: str = "sqlite:///./test.db"  # ค่า default สำหรับ SQLite
    SECRET_KEY: str = "secret"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 5 * 60  # 5 ชั่วโมง
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 7 * 24 * 60  # 7 วัน

    model_config = {
        "env_file": ".env",
        "validate_assignment": True,
        "extra": "allow"
    }

def get_settings():
    return Settings()