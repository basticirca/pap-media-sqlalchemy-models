"""Preset model"""
from database.base import TableBase
from enum import IntEnum

from sqlalchemy import Column, String, Enum, Text


class PresetType(IntEnum):
    unknown = 0
    playlist = 1
    nested = 2
    map = 3


class Preset(TableBase):

    __tablename__ = 'preset'

    uuid = Column(String(64), primary_key=True)

    name = Column(String(128), nullable=False)

    description = Column(String(512))

    type = Column(Enum(PresetType), default=PresetType.unknown, nullable=False)

    json = Column(Text, nullable=False)

    # definition see tables.tag
    tags = []

    def __repr__(self):
        return "<Preset uuid=%s name=%s description=%s type=%s json=[size:%s]>" % (
            self.uuid, self.name, self.description, str(self.type), len(self.json))
