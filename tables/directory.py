"""Directory model"""
from database.base import TableBase
from database.tables import associations

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Directory(TableBase):

    __tablename__ = 'directory'

    uuid = Column(String(64), primary_key=True)

    name = Column(String(128), nullable=False)

    children = relationship(
        "Directory",
        secondary=associations.directory_hierarchie,
        primaryjoin=(uuid == associations.directory_hierarchie.c.parent_uuid),
        secondaryjoin=(uuid == associations.directory_hierarchie.c.child_uuid),
        backref="parents"
    )

    parents = []

    resources = relationship(
        "Resource",
        secondary=associations.directory_resource,
        backref="directories"
    )

    def __repr__(self):
        return "<Directory uuid=%s name=%s>" % (
            self.uuid, self.name)
