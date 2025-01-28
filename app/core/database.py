from typing import AsyncGenerator
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.ext.asyncio import (AsyncSession, AsyncAttrs, async_sessionmaker,
                                    create_async_engine)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.core.config import setting


class Base(AsyncAttrs, DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())


engine = create_async_engine(
    url=setting.db.url,
    echo=setting.db.echo,
)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
