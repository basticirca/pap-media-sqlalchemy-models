""" lookup table definitions for describing relationship associations """
import database.constants
from database.base import TableBase

from sqlalchemy import Column, Table
from sqlalchemy import ForeignKey

###
# directory
###

directory_hierarchie = Table(
    "directory_hierarchie", TableBase.metadata,
    Column(
        "parent_uuid",
        ForeignKey(
            "directory.uuid", name="a",
            onupdate=database.constants.CASCADE, ondelete=database.constants.CASCADE
        ),
        primary_key=True
    ),
    Column(
        "child_uuid",
        ForeignKey(
            "directory.uuid", name="b",
            onupdate=database.constants.CASCADE, ondelete=database.constants.CASCADE
        ),
        primary_key=True
    )
)

directory_resource = Table(
    "directory_resource", TableBase.metadata,
    Column(
        "directory_uuid",
        ForeignKey(
            "directory.uuid", name="a",
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

###
# tag
###

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

###
# tag
###

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
