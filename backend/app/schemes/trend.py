import datetime

from pydantic import Field

from .base import CamelModel


class Trend(CamelModel):
    title: str
    date: datetime.date
    topic: list[str] = Field(default_factory=[])


class TrendORM(Trend):
    id: int

    class Config:
        orm_mode = True


class TrendWithFavoriteORM(TrendORM):
    favorite: bool
