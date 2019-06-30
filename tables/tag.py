"""Tag model"""
from database.base import TableBase
from sqlalchemy import Column, String


class Tag(TableBase):

    __tablename__ = 'tag'

    uuid = Column(String(64), primary_key=True)

    name = Column(String(128), nullable=False)

    description = Column(String(512))

    def __repr__(self):
        return "<Tag uuid=%s name=%s description=%s>" % (
            self.uuid, self.name, self.description)
