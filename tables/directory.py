"""Directory model"""
from database.base import TableBase
import database.constants

from sqlalchemy import Column, String, Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


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


class Directory(TableBase):

    __tablename__ = 'directory'

    uuid = Column(String(64), primary_key=True)

    name = Column(String(128), nullable=False)

    children = relationship(
        "Directory",
        secondary=directory_hierarchie,
        primaryjoin=uuid == directory_hierarchie.c.parent_uuid,
        secondaryjoin=uuid == directory_hierarchie.c.child_uuid,
        backref="parents"
    )

    resources = relationship("DirectoryResource", back_populates="directory")

    def __repr__(self):
        return "<Directory uuid=%s name=%s>" % (
            self.uuid, self.name)
