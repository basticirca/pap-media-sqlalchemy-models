"""Playlist model"""
from database.base import TableBase
from sqlalchemy import Column, String


class Playlist(TableBase):

    __tablename__ = 'playlist'

    uuid = Column(String(64), primary_key=True)

    name = Column(String(128), nullable=False)

    description = Column(String(512))

    # definition see tables.tag
    tags = []

    def __repr__(self):
        return "<Playlist uuid=%s name=%s description=%s>" % (
            self.uuid, self.name, self.description)
