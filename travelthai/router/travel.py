from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..model import travel
from travelthai.schemas.schema import UserCreate, UserRead, UserLogin, RegistrationCreate, RegistrationRead, ProvinceRead
from ..core.dependencie import get_current_user

router = APIRouter()

@router.post("/register", response_model=RegistrationRead)
def register_travel(info: RegistrationCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_reg = travel.Registration(
        user_id=user.id,
        full_name=info.full_name,
        citizen_id=info.citizen_id,
        phone=info.phone,
        target_province=info.target_province
    )
    db.add(db_reg)
    db.commit()
    db.refresh(db_reg)
    return db_reg

@router.get("/provinces", response_model=list[ProvinceRead])
def get_provinces(db: Session = Depends(get_db)):
    return db.query(travel.Province).all()

@router.get("/provinces/{province_id}", response_model=ProvinceRead)
def get_province(province_id: int, db: Session = Depends(get_db)):
    province = db.query(travel.Province).filter(travel.Province.id == province_id).first()
    if not province:
        raise HTTPException(status_code=404, detail="Province not found")
    return province

@router.get("/provinces/{province_id}/tax-reduction")
def get_tax_reduction(province_id: int, db: Session = Depends(get_db)):
    province = db.query(travel.Province).filter(travel.Province.id == province_id).first()
    if not province:
        raise HTTPException(status_code=404, detail="Province not found")
    return {"province": province.name, "tax_reduction": province.tax_reduction, "is_secondary": province.is_secondary}

@router.get("/registers", response_model=list[RegistrationRead])
def get_all_registrations(db: Session = Depends(get_db)):
    return db.query(travel.Registration).all()

@router.get("/registers/user/{user_id}", response_model=list[RegistrationRead])
def get_registrations_by_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(travel.Registration).filter(travel.Registration.user_id == user_id).all()