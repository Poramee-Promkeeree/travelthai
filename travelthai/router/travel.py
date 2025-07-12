from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..model import travel, schemas
from ..core.dependencie import get_current_user

router = APIRouter()

@router.post("/register", response_model=schemas.RegistrationRead)
def register_travel(info: schemas.RegistrationCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
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

@router.get("/provinces", response_model=list[schemas.ProvinceRead])
def get_provinces(db: Session = Depends(get_db)):
    return db.query(travel.Province).all()

@router.get("/provinces/{province_id}", response_model=schemas.ProvinceRead)
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