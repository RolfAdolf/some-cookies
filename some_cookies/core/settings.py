from pydantic import BaseSettings
from pydantic.error_wrappers import ValidationError


class Settings(BaseSettings):
    driver_path: str
    database_path: str
    news_url: str
    max_delay: int
    max_processes: int


try:
    settings = Settings(_env_file="./.env", _env_file_encoding="utf-8")
except ValidationError:
    settings = Settings(_env_file="../.env", _env_file_encoding="utf-8")
