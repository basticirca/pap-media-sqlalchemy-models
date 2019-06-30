"""Directory model"""
from database.base import TableBase
import database.constants

from sqlalchemy import Column, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Directory(TableBase):

    __tablename__ = 'directory'

    uuid = Column(String(64), primary_key=True)

    name = Column(String(128), nullable=False)

    parent_uuid = Column(
        String(64),
        ForeignKey("directory.uuid", onupdate=database.constants.CASCADE, ondelete=database.constants.CASCADE),
        nullable=True
    )

    parent = relationship("Directory", uselist=False)

    resources = relationship("DirectoryResource", back_populates="directory")

    def __repr__(self):
        return "<Directory uuid=%s name=%s parent_uuid=%s>" % (
            self.uuid, self.name, self.parent_uuid)
