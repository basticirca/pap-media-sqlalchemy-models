import constants
from base import TableBase

from sqlalchemy import Column, Table
from sqlalchemy import ForeignKey

album_image = Table(
    "album_image", TableBase.metadata,
    Column(
        "album_uuid",
        ForeignKey(
            "album.uuid", name="a",
            onupdate=constants.CASCADE, ondelete=constants.CASCADE
        ),
        primary_key=True
    ),
    Column(
        "image_uuid",
        ForeignKey(
            "image.uuid", name="b",
            onupdate=constants.CASCADE, ondelete=constants.CASCADE
        ),
        primary_key=True
    )
)