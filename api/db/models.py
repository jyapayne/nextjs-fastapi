from typing import List
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .engine import engine


class Base(DeclarativeBase):
    pass


def create_tables():
    Base.metadata.create_all(engine)
