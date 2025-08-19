# backend/app/models/user.py

from sqlalchemy import Column, Integer, String
from ..database import Base  # import relativo

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    role = Column(String, index=True)  # "coder" o "admin"
