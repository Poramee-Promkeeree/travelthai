from sqlalchemy import Column, Integer, String, Float
from ..database import Base

class Registration(Base):
    __tablename__ = "registrations"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    citizen_id = Column(String, nullable=False)  # เอา unique ออก
    phone = Column(String, nullable=False)
    target_province = Column(String, nullable=False)

class Province(Base):
    __tablename__ = "provinces"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    is_secondary = Column(Integer, default=0)  # 1 = secondary, 0 = primary
    tax_reduction = Column(Float, default=0.0)

def seed_provinces(db):
    provinces = [
        {"name": "Bangkok", "is_secondary": 0, "tax_reduction": 5.0},
        {"name": "Chiang Mai", "is_secondary": 0, "tax_reduction": 5.0},
        {"name": "Nan", "is_secondary": 1, "tax_reduction": 10.0},
        {"name": "Loei", "is_secondary": 1, "tax_reduction": 10.0},
        {"name": "Trang", "is_secondary": 1, "tax_reduction": 10.0},
        {"name": "Phatthalung", "is_secondary": 1, "tax_reduction": 10.0},
    ]
    for p in provinces:
        exists = db.query(Province).filter(Province.name == p["name"]).first()
        if not exists:
            db.add(Province(**p))
    db.commit()
