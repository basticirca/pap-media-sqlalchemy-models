"""SoundFile model"""
from database.base import TableBase
import database.constants

from sqlalchemy import Column, Integer, String

class SoundFile(TableBase):
  """SoundFile database object"""

  __tablename__ = 'sound_file'

  id = Column(Integer, primary_key=True)

  uuid = Column(String(64), nullable=False, unique=True)

  name = Column(String(256), nullable=False)
  
  path = Column(String(512), nullable=False, unique=True)
  
  relative_path = Column(String(512), nullable=False)
  
  def __repr__(self):
    return "<SoundFile id=%s uuid=%s name=%s path=%s relative_path=%s>" % (
        str(self.id), self.uuid, self.name, self.path, self.relative_path)
