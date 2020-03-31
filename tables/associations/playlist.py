import constants
from base import TableBase

from sqlalchemy import Column, Table
from sqlalchemy import ForeignKey

playlist_sound = Table(
    "playlist_sound", TableBase.metadata,
    Column(
        "playlist_uuid",
        ForeignKey(
            "playlist.uuid", name="a",
            onupdate=constants.CASCADE, ondelete=constants.CASCADE
        ),
        primary_key=True
    ),
    Column(
        "sound_uuid",
        ForeignKey(
            "sound.uuid", name="b",
            onupdate=constants.CASCADE, ondelete=constants.CASCADE
        ),
        primary_key=True
    )
)