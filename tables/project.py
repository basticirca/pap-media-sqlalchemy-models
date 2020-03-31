"""Project model"""
from base import TableBase

from sqlalchemy import Column, String, Text


class Project(TableBase):

    __tablename__ = 'project'

    uuid = Column(String(64), primary_key=True)

    name = Column(String(128), nullable=False)

    description = Column(String(512))

    json = Column(Text, nullable=False)

    # definition see tables.tag
    tags = []

    def __repr__(self):
        return "<Project uuid=%s name=%s description=%s json=[size:%s]>" % (
            self.uuid, self.name, self.description, len(self.json))
