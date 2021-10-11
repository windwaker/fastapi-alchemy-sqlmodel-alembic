from datetime import datetime

from sqlmodel import SQLModel, Field

from typing import Optional


class SongBase(SQLModel):
    name: str
    artist: str
    year: Optional[int] = None


class Song(SongBase, table=True):
    id: int = Field(default=None, primary_key=True)


class SongCreate(SongBase):
    pass


class PlayerBase(SQLModel):
    name: str  # = Field(min_length=2, max_length=50, )
    # https://pydantic-docs.helpmanual.io/usage/types/#datetime-types
    date_of_birth: str  # datetime = Field(default=None)


class Player(PlayerBase, table=True):
    id: int = Field(default=None, primary_key=True)
