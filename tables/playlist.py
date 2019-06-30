"""Playlist model"""
from database.base import TableBase
from database.tables import associations

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Playlist(TableBase):

    __tablename__ = 'playlist'

    uuid = Column(String(64), primary_key=True)

    name = Column(String(128), nullable=False)

    description = Column(String(512))

    sounds = relationship("Sound", secondary=associations.tag_playlist, backref="playlists")

    # definition see tables.tag
    tags = []

    def __repr__(self):
        return "<Playlist uuid=%s name=%s description=%s>" % (
            self.uuid, self.name, self.description)
