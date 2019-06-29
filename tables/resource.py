"""Resource model"""
from database.base import TableBase
import enum

from sqlalchemy import Column, Integer, String, Enum


class ResourceType(enum.Enum):
    unknown = 0
    sound = 1
    image = 2


class Resource(TableBase):

    __tablename__ = 'resource'

    uuid = Column(String(64), primary_key=True)

    name = Column(String(128))

    type = Column(Enum(ResourceType), default=ResourceType.unknown, nullable=False)

    def __repr__(self):
        return "<SoundFile id=%s uuid=%s type=%s name=%s>" % (
            str(self.id), self.uuid, str(self.type), self.name)
