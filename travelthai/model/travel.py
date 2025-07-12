from sqlalchemy import Column, Integer, String
from ..database import Base

class Registration(Base):
    __tablename__ = "registrations"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    citizen_id = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)
    target_province = Column(String, nullable=False)
