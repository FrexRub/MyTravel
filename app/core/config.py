import logging
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent.parent


# COOKIE_NAME = "app_travel"


def configure_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
    )


class SettingConn(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int

    BOT_TOKEN: str
    BASE_SITE: str
    ADMIN_ID: str

    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env")


setting_conn = SettingConn()


class DbSetting(BaseSettings):
    url: str = (
        f"postgresql+asyncpg://{setting_conn.postgres_user}:{setting_conn.postgres_password}@{setting_conn.postgres_host}:{setting_conn.postgres_port}/{setting_conn.postgres_db}"
    )
    echo: bool = False


class Setting(BaseSettings):
    db: DbSetting = DbSetting()

    def get_webhook_url(self) -> str:
        """Возвращает URL вебхука с кодированием специальных символов."""
        return f"{setting_conn.BASE_SITE}/webhook"


setting = Setting()
