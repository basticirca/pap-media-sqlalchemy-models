import database.constants
from database.base import TableBase

from sqlalchemy import Column, Table
from sqlalchemy import ForeignKey

album_image = Table(
    "album_image", TableBase.metadata,
    Column(
        "album_uuid",
        ForeignKey(
            "album.uuid", name="a",
            onupdate=database.constants.CASCADE, ondelete=database.constants.CASCADE
        ),
        primary_key=True
    ),
    Column(
        "image_uuid",
        ForeignKey(
            "image.uuid", name="b",
            onupdate=database.constants.CASCADE, ondelete=database.constants.CASCADE
        ),
        primary_key=True
    )
)