"""Image model"""
from database.base import TableBase
import database.constants

from sqlalchemy import Column, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class World(TableBase):

    __tablename__ = 'image'

    uuid = Column(String(64), primary_key=True)

    name = Column(String(128), nullable=False)

    description = Column(String(512), nullable=True)

    image = relationship("Image", uselist=False)

    def __repr__(self):
        return "<World uuid=%s>" % (
            str(self.uuid))
