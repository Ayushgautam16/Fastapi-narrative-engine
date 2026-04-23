from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from db.database import Base


class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    session_id = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    nodes = relationship("StoryNode", back_populates="story")


