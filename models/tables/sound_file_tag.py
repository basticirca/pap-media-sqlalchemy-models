"""SoundFileTag model"""
from database.base import TableBase
import database.constants

from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Index

class SoundFileTag(TableBase):
  """SoundFileTag database object"""

  __tablename__ = 'sound_file_tag'

  id = Column(Integer, primary_key=True)

  sound_file_id = Column(
    Integer, 
    ForeignKey("sound_file.id", onupdate=database.constants.CASCADE, ondelete=database.constants.CASCADE),
    nullable=False
  )
  
  tag_id = Column(
    Integer, 
    ForeignKey("tag.id", onupdate=database.constants.CASCADE, ondelete=database.constants.CASCADE),
    nullable=False
  )
  
  sound_file = relationship("SoundFile", uselist=False)
  tag = relationship("Tag", uselist=False)
  
  u_idx = Index(
    'sound_file_tag_uidx',
    sound_file_id, tag_id,
    unique=True
  )
  
  def __repr__(self):
    return "<SoundFileTag id=%s sound_file_id=%s tag_id=%s>" % (
        str(self.id), self.sound_file_id, self.tag_id)
