# backend/app/routes/users.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models.user import User

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# Dependencia para obtener sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----------- CREATE -----------
@router.post("/")
def create_user(name: str, role: str, db: Session = Depends(get_db)):
    new_user = User(name=name, role=role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# ----------- READ ALL -----------
@router.get("/")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()

# ----------- READ BY ID -----------
@router.get("/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

# ----------- UPDATE -----------
@router.put("/{user_id}")
def update_user(user_id: int, name: str, role: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    user.name = name
    user.role = role
    db.commit()
    db.refresh(user)
    return user

# ----------- DELETE -----------
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(user)
    db.commit()
    return {"detail": f"Usuario con ID {user_id} eliminado"}
