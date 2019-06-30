import database.constants
from database.base import TableBase

from sqlalchemy import Column, Table
from sqlalchemy import ForeignKey

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