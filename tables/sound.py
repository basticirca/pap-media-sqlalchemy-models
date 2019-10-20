"""SoundFile model"""
from database.base import TableBase
import database.constants

from sqlalchemy import Column, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Sound(TableBase):

    __tablename__ = 'sound'

    uuid = Column(
        String(64),
        ForeignKey("resource.uuid", onupdate=database.constants.CASCADE, ondelete=database.constants.CASCADE),
        primary_key=True
    )

    local_path = Column(String(256), nullable=True)

    resource = relationship("Resource", uselist=False)

    playlists = []

    def __repr__(self):
        return "<Sound uuid=%s>" % (
            str(self.uuid))
