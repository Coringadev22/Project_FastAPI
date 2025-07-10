from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from models import User, Session
from typing import List, Optional

user_router = APIRouter(prefix="/users", tags=["users"])

session = Session()

@user_router.get("/", response_model=List[dict])
async def get_users():
    users = session.query(User).all()
    result = []
    for user in users:
        result.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "admin": user.admin,
            "active": user.active,
            "created_at": user.created_at,
            "updated_at": user.updated_at
        })
    return result

@user_router.get("/{user_id}", response_model=dict)
async def get_user(user_id: int):
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "admin": user.admin,
        "active": user.active,
        "created_at": user.created_at,
        "updated_at": user.updated_at
    }

from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    admin: bool = False
    active: bool = True

@user_router.post("/", response_model=dict)
async def create_user(user: UserCreate):
    db_user = User(
        name=user.name,
        email=user.email,
        password=user.password,
        admin=user.admin,
        active=user.active
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return {
        "id": db_user.id,
        "name": db_user.name,
        "email": db_user.email,
        "admin": db_user.admin,
        "active": db_user.active,
        "created_at": db_user.created_at,
        "updated_at": db_user.updated_at
    }

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    admin: Optional[bool] = None
    active: Optional[bool] = None

@user_router.put("/{user_id}", response_model=dict)
async def update_user(user_id: int, user: UserUpdate):
    db_user = session.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    if user.name is not None:
        db_user.name = user.name
    if user.email is not None:
        db_user.email = user.email
    if user.password is not None:
        db_user.password = user.password
    if user.admin is not None:
        db_user.admin = user.admin
    if user.active is not None:
        db_user.active = user.active
    session.commit()
    session.refresh(db_user)
    return {
        "id": db_user.id,
        "name": db_user.name,
        "email": db_user.email,
        "admin": db_user.admin,
        "active": db_user.active,
        "created_at": db_user.created_at,
        "updated_at": db_user.updated_at
    }

@user_router.delete("/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    db_user = session.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    session.delete(db_user)
    session.commit()
    return {"message": "Usuário deletado com sucesso"}
