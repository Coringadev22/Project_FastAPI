from fastapi import APIRouter, HTTPException
from models import Session, Delivery_Man, Motocycle, Store, Customer
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


delivery_man_router = APIRouter(prefix="/deliveryman", tags=["deliveryman"])

session = Session()

class DeliveryManCreate(BaseModel):
    name: str
    phone: str
    cpf: str
    cnh: str
    cnh_expiration: str  # ISO format date string
    active: Optional[bool] = True

class DeliveryManUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    cpf: Optional[str] = None
    cnh: Optional[str] = None
    cnh_expiration: Optional[str] = None  # ISO format
    active: Optional[bool] = None

@delivery_man_router.get("/", response_model=List[dict])
async def get_deliverymen():
    deliverymen = session.query(Delivery_Man).all()
    result = []
    for d in deliverymen:
        result.append({ 
            "id": d.id,
            "name": d.name,
            "phone": d.phone,
            "cpf": d.cpf,
            "cnh": d.cnh,
            "cnh_expiration": d.cnh_expiration,
            "active": d.active,
            "created_at": d.created_at,
            "updated_at": d.updated_at
        })
    return result

@delivery_man_router.get("/{deliveryman_id}", response_model=dict)
async def get_deliveryman(deliveryman_id: int):
    d = session.query(Delivery_Man).filter(Delivery_Man.id == deliveryman_id).first()
    if not d:
        raise HTTPException(status_code=404, detail="Entregador não encontrado")
    return {
        "id": d.id,
        "name": d.name,
        "phone": d.phone,
        "cpf": d.cpf,
        "cnh": d.cnh,
        "cnh_expiration": d.cnh_expiration,
        "active": d.active,
        "created_at": d.created_at,
        "updated_at": d.updated_at
    }

@delivery_man_router.post("/", response_model=dict)
async def create_deliveryman(deliveryman: DeliveryManCreate):
    db_deliveryman = Delivery_Man(
        name=deliveryman.name,
        email=deliveryman.email,
        password=deliveryman.password,
        phone=deliveryman.phone,
        cpf=deliveryman.cpf,
        cnh=deliveryman.cnh,
        cnh_expiration=deliveryman.cnh_expiration,
        active=deliveryman.active
    )
    session.add(db_deliveryman)
    session.commit()
    session.refresh(db_deliveryman)
    return {
        "id": db_deliveryman.id,
        "name": db_deliveryman.name,
        "phone": db_deliveryman.phone,
        "cpf": db_deliveryman.cpf,
        "cnh": db_deliveryman.cnh,
        "cnh_expiration": db_deliveryman.cnh_expiration,
        "active": db_deliveryman.active,
        "created_at": db_deliveryman.created_at,
        "updated_at": db_deliveryman.updated_at
    }

@delivery_man_router.put("/{deliveryman_id}", response_model=dict)
async def update_deliveryman(deliveryman_id: int, deliveryman: DeliveryManUpdate):
    db_deliveryman = session.query(Delivery_Man).filter(Delivery_Man.id == deliveryman_id).first()
    if not db_deliveryman:
        raise HTTPException(status_code=404, detail="Entregador não encontrado")
    if deliveryman.name is not None:
        db_deliveryman.name = deliveryman.name
    if deliveryman.phone is not None:
        db_deliveryman.phone = deliveryman.phone
    if deliveryman.cpf is not None:
        db_deliveryman.cpf = deliveryman.cpf
    if deliveryman.cnh is not None:
        db_deliveryman.cnh = deliveryman.cnh
    if deliveryman.cnh_expiration is not None:
        db_deliveryman.cnh_expiration = datetime.fromisoformat(deliveryman.cnh_expiration)
    if deliveryman.active is not None:
        db_deliveryman.active = deliveryman.active
    session.commit()
    session.refresh(db_deliveryman)
    return {
        "id": db_deliveryman.id,
        "name": db_deliveryman.name,
        "phone": db_deliveryman.phone,
        "cpf": db_deliveryman.cpf,
        "cnh": db_deliveryman.cnh,
        "cnh_expiration": db_deliveryman.cnh_expiration,
        "active": db_deliveryman.active,
        "created_at": db_deliveryman.created_at,
        "updated_at": db_deliveryman.updated_at
    }

@delivery_man_router.delete("/{deliveryman_id}", response_model=dict)
async def delete_deliveryman(deliveryman_id: int):
    db_deliveryman = session.query(Delivery_Man).filter(Delivery_Man.id == deliveryman_id).first()
    if not db_deliveryman:
        raise HTTPException(status_code=404, detail="Entregador não encontrado")
    session.delete(db_deliveryman)
    session.commit()
    return {"message": "Entregador deletado com sucesso"}
