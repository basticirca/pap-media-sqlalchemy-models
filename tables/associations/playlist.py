import database.constants
from database.base import TableBase

from sqlalchemy import Column, Table
from sqlalchemy import ForeignKey

playlist_sound = Table(
    "playlist_sound", TableBase.metadata,
    Column(
        "playlist_uuid",
        ForeignKey(
            "playlist.uuid", name="a",
            onupdate=database.constants.CASCADE, ondelete=database.constants.CASCADE
        ),
        primary_key=True
    ),
    Column(
        "sound_uuid",
        ForeignKey(
            "sound.uuid", name="b",
            onupdate=database.constants.CASCADE, ondelete=database.constants.CASCADE
        ),
        primary_key=True
    )
)