"""ImageDirectory model"""
from database.base import TableBase
import database.constants

from sqlalchemy import Column, Integer, String

class ImageDirectory(TableBase):
  """ImageDirectory database object"""

  __tablename__ = 'image_directory'

  id = Column(Integer, primary_key=True)

  path = Column(String(512), unique=True)
  
  def __repr__(self):
    return "<ImageDirectory id=%s path=%s>" % (
        str(self.id), self.path)
