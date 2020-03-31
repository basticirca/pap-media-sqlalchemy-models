"""Album model"""
from base import TableBase
from tables import associations

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Album(TableBase):

    __tablename__ = 'album'

    uuid = Column(String(64), primary_key=True)

    name = Column(String(128), nullable=False)

    description = Column(String(512))

    images = relationship("Image", secondary=associations.album_image, backref="albums")

    # definition see tables.tag
    tags = []

    def __repr__(self):
        return "<Album uuid=%s name=%s description=%s>" % (
            self.uuid, self.name, self.description)
