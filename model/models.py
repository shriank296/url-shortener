from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from base import Model
from uuid import uuid4

class UrlMapper(Model):
    __tablename__="url_mappers"

    id: Mapped[int] = mapped_column(primary_key=True)
    original_url: Mapped[str] = mapped_column(Text)
    short_url: Mapped[str] = mapped_column(String(16), index=True, unique=True)

    def __repr__(self) -> str:
        return f'id:{self.id}, short_url: {self.short_url}'