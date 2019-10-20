"""Image model"""
from database.base import TableBase
import database.constants

from sqlalchemy import Column, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Image(TableBase):

    __tablename__ = 'image'

    uuid = Column(
        String(64),
        ForeignKey("resource.uuid", onupdate=database.constants.CASCADE, ondelete=database.constants.CASCADE),
        primary_key=True
    )

    resource = relationship("Resource", uselist=False)

    local_path = Column(String(256), nullable=True)

    albums = []

    def __repr__(self):
        return "<Image uuid=%s>" % (
            str(self.uuid))
