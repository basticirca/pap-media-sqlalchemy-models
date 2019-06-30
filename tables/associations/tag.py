import database.constants
from database.base import TableBase

from sqlalchemy import Column, Table
from sqlalchemy import ForeignKey

tag_resource = Table(
    "tag_resource", TableBase.metadata,
    Column(
        "tag_uuid",
        ForeignKey(
            "tag.uuid", name="a",
            onupdate=database.constants.CASCADE, ondelete=database.constants.CASCADE
        ),
        primary_key=True
    ),
    Column(
        "resource_uuid",
        ForeignKey(
            "resource.uuid", name="b",
            onupdate=database.constants.CASCADE, ondelete=database.constants.CASCADE
        ),
        primary_key=True
    )
)

tag_preset = Table(
    "tag_preset", TableBase.metadata,
    Column(
        "tag_uuid",
        ForeignKey(
            "tag.uuid", name="a",
            onupdate=database.constants.CASCADE, ondelete=database.constants.CASCADE
        ),
        primary_key=True
    ),
    Column(
        "preset_uuid",
        ForeignKey(
            "preset.uuid", name="b",
            onupdate=database.constants.CASCADE, ondelete=database.constants.CASCADE
        ),
        primary_key=True
    )
)

tag_project = Table(
    "tag_project", TableBase.metadata,
    Column(
        "tag_uuid",
        ForeignKey(
            "tag.uuid", name="a",
            onupdate=database.constants.CASCADE, ondelete=database.constants.CASCADE
        ),
        primary_key=True
    ),
    Column(
        "project_uuid",
        ForeignKey(
            "project.uuid", name="b",
            onupdate=database.constants.CASCADE, ondelete=database.constants.CASCADE
        ),
        primary_key=True
    )
)

tag_playlist = Table(
    "tag_playlist", TableBase.metadata,
    Column(
        "tag_uuid",
        ForeignKey(
            "tag.uuid", name="a",
            onupdate=database.constants.CASCADE, ondelete=database.constants.CASCADE
        ),
        primary_key=True
    ),
    Column(
        "playlist_uuid",
        ForeignKey(
            "playlist.uuid", name="b",
            onupdate=database.constants.CASCADE, ondelete=database.constants.CASCADE
        ),
        primary_key=True
    )
)

tag_album = Table(
    "tag_album", TableBase.metadata,
    Column(
        "tag_uuid",
        ForeignKey(
            "tag.uuid", name="a",
            onupdate=database.constants.CASCADE, ondelete=database.constants.CASCADE
        ),
        primary_key=True
    ),
    Column(
        "album_uuid",
        ForeignKey(
            "album.uuid", name="b",
            onupdate=database.constants.CASCADE, ondelete=database.constants.CASCADE
        ),
        primary_key=True
    )
)