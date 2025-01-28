from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True
    )  # Уникальный идентификатор пользователя в Telegram
    first_name: Mapped[str] = mapped_column(String, nullable=False)  # Имя пользователя
    username: Mapped[str] = mapped_column(String, nullable=True)  # Telegram username
