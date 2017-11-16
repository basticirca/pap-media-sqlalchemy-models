"""Preset model"""
from database.base import TableBase
import database.constants

from sqlalchemy import Column, Integer, String

class Preset(TableBase):
  """Preset database object"""

  __tablename__ = 'preset'

  id = Column(Integer, primary_key=True)
  
  name = Column(String(256), nullable=False)
  
  json = Column(String(4096), nullable=False)
  
  def __repr__(self):
    return "<Preset id=%s name=%s json=%s>" % (
        str(self.id), self.name, self.json)
