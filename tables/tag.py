"""Tag model"""
from database.base import TableBase
from database.tables import associations

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Tag(TableBase):

    __tablename__ = 'tag'

    uuid = Column(String(64), primary_key=True)

    name = Column(String(128), nullable=False)

    description = Column(String(512))

    resources = relationship("Resource", secondary=associations.tag_resource, backref="tags")

    presets = relationship("Preset", secondary=associations.tag_preset, backref="tags")

    projects = relationship("Project", secondary=associations.tag_project, backref="tags")

    playlists = relationship("Playlist", secondary=associations.tag_playlist, backref="tags")

    def __repr__(self):
        return "<Tag uuid=%s name=%s description=%s>" % (
            self.uuid, self.name, self.description)
