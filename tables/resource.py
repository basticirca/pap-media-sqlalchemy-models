"""Resource model"""
from database.base import TableBase
from enum import IntEnum

from sqlalchemy import Column, Integer, String, Enum


class ResourceType(IntEnum):
    unknown = 0
    sound = 1
    image = 2


class Resource(TableBase):

    __tablename__ = 'resource'

    uuid = Column(String(64), primary_key=True)

    name = Column(String(128))

    type = Column(Enum(ResourceType), default=ResourceType.unknown, nullable=False)

    # relationship defined in tables.directory
    directories = []

    # definition see tables.tag
    tags = []

    def __repr__(self):
        return "<Resource uuid=%s type=%s name=%s>" % (
            self.uuid, str(self.type), self.name)
