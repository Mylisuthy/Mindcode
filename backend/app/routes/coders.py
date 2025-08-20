from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models.user import User


# ------------- router from coders ---------------
router = APIRouter(
    prefix="/coders",
    tags=["coders"]
)

# ------------ route for coders ---------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def list_coders(db: Session = Depends(get_db)):
    coders = db.query(User).filter(User.role == "coder").all()
    return coders