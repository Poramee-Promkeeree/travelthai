from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Registration
from ..schemas import RegistrationCreate, RegistrationRead
from ..core.dependencie import get_current_user

router = APIRouter()

@router.post("/register", response_model=RegistrationRead)
def register_travel(info: RegistrationCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_reg = Registration(
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