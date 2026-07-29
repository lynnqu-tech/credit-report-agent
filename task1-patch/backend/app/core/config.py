from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    secret_key: str
    database_url: str = "postgresql+psycopg://credit:credit@db:5432/credit"
    redis_url: str = "redis://redis:6379/0"
    qwen_api_key: str = ""
    qwen_base_url: str = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    qwen_chat_model: str = "qwen-plus"
    qwen_embedding_model: str = "text-embedding-v4"
    storage_root: Path = Path("/data/uploads")
    export_root: Path = Path("/data/exports")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
