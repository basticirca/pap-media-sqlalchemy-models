"""SoundFile model"""
from base import TableBase
import constants

from sqlalchemy import Column, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Sound(TableBase):

    __tablename__ = 'sound'

    uuid = Column(
        String(64),
        ForeignKey("resource.uuid", onupdate=constants.CASCADE, ondelete=constants.CASCADE),
        primary_key=True
    )

    local_path = Column(String(256), nullable=True)

    resource = relationship("Resource", uselist=False)

    playlists = []

    def __repr__(self):
        return "<Sound uuid=%s>" % (
            str(self.uuid))
