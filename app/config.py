import logging
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent

# COOKIE_NAME = "app_travel"


def configure_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
    )


class Setting(BaseSettings):
    BOT_TOKEN: str
    BASE_SITE: str
    ADMIN_ID: str

    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env")


setting = Setting()
