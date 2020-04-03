"""User model"""
from base import TableBase

from sqlalchemy import Column, String


class User(TableBase):

    __tablename__ = 'user'

    uuid = Column(String(128), primary_key=True)

    name = Column(String(64), nullable=False)

    email = Column(String(64), unique=True, nullable=False)

    profile_pic = Column(String(256), nullable=False)

    def __repr__(self):
        return "<User id=%s name=%s email=%s profile_pic=%s>" % (
            str(self.id), str(self.name), str(self.email), str(self.profile_pic))
