"""DirectoryResource model"""
from database.base import TableBase
import database.constants

from sqlalchemy import Column, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class DirectoryResource(TableBase):

    __tablename__ = 'directory_resource'

    directory_uuid = Column(
        String(64),
        ForeignKey("directory.uuid", onupdate=database.constants.CASCADE, ondelete=database.constants.CASCADE),
        primary_key=True
    )

    resource_uuid = Column(
        String(64),
        ForeignKey("resource.uuid", onupdate=database.constants.CASCADE, ondelete=database.constants.CASCADE),
        primary_key=True
    )

    directory = relationship("Directory", back_populates="resources")

    resource = relationship("Resource", uselist=False)

    def __repr__(self):
        return "<Directory directory_uuid=%s image_uuid=%s>" % (
            self.directory_uuid, self.image_uuid)
