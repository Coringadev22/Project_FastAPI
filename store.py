from fastapi import APIRouter, HTTPException
from models import Session, Store
from typing import List, Optional
from pydantic import BaseModel

store_router = APIRouter(prefix="/store", tags=["store"])

session = Session()

class StoreCreate(BaseModel):
    name: str
    phone: str
    address: str
    number: str
    complement: str
    neighborhood: str
    city: str
    state: str
    zip_code: str
    active: Optional[bool] = True

class StoreUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    number: Optional[str] = None
    complement: Optional[str] = None
    neighborhood: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    active: Optional[bool] = None

@store_router.get("/", response_model=List[dict])
async def get_stores():
    stores = session.query(Store).all()
    result = []
    for s in stores:
        result.append({
            "id": s.id,
            "name": s.name,
            "phone": s.phone,
            "address": s.address,
            "number": s.number,
            "complement": s.complement,
            "neighborhood": s.neighborhood,
            "city": s.city,
            "state": s.state,
            "zip_code": s.zip_code,
            "active": s.active,
            "created_at": s.created_at,
            "updated_at": s.updated_at
        })
    return result

@store_router.get("/{store_id}", response_model=dict)
async def get_store(store_id: int):
    s = session.query(Store).filter(Store.id == store_id).first()
    if not s:
        raise HTTPException(status_code=404, detail="Loja não encontrada")
    return {
        "id": s.id,
        "name": s.name,
        "phone": s.phone,
        "address": s.address,
        "number": s.number,
        "complement": s.complement,
        "neighborhood": s.neighborhood,
        "city": s.city,
        "state": s.state,
        "zip_code": s.zip_code,
        "active": s.active,
        "created_at": s.created_at,
        "updated_at": s.updated_at
    }

@store_router.post("/", response_model=dict)
async def create_store(store: StoreCreate):
    db_store = Store(
        name=store.name,
        phone=store.phone,
        address=store.address,
        number=store.number,
        complement=store.complement,
        neighborhood=store.neighborhood,
        city=store.city,
        state=store.state,
        zip_code=store.zip_code,
        active=store.active
    )
    session.add(db_store)
    session.commit()
    session.refresh(db_store)
    return {
        "id": db_store.id,
        "name": db_store.name,
        "phone": db_store.phone,
        "address": db_store.address,
        "number": db_store.number,
        "complement": db_store.complement,
        "neighborhood": db_store.neighborhood,
        "city": db_store.city,
        "state": db_store.state,
        "zip_code": db_store.zip_code,
        "active": db_store.active,
        "created_at": db_store.created_at,
        "updated_at": db_store.updated_at
    }

@store_router.put("/{store_id}", response_model=dict)
async def update_store(store_id: int, store: StoreUpdate):
    db_store = session.query(Store).filter(Store.id == store_id).first()
    if not db_store:
        raise HTTPException(status_code=404, detail="Loja não encontrada")
    if store.name is not None:
        db_store.name = store.name
    if store.phone is not None:
        db_store.phone = store.phone
    if store.address is not None:
        db_store.address = store.address
    if store.number is not None:
        db_store.number = store.number
    if store.complement is not None:
        db_store.complement = store.complement
    if store.neighborhood is not None:
        db_store.neighborhood = store.neighborhood
    if store.city is not None:
        db_store.city = store.city
    if store.state is not None:
        db_store.state = store.state
    if store.zip_code is not None:
        db_store.zip_code = store.zip_code
    if store.active is not None:
        db_store.active = store.active
    session.commit()
    session.refresh(db_store)
    return {
        "id": db_store.id,
        "name": db_store.name,
        "phone": db_store.phone,
        "address": db_store.address,
        "number": db_store.number,
        "complement": db_store.complement,
        "neighborhood": db_store.neighborhood,
        "city": db_store.city,
        "state": db_store.state,
        "zip_code": db_store.zip_code,
        "active": db_store.active,
        "created_at": db_store.created_at,
        "updated_at": db_store.updated_at
    }

@store_router.delete("/{store_id}", response_model=dict)
async def delete_store(store_id: int):
    db_store = session.query(Store).filter(Store.id == store_id).first()
    if not db_store:
        raise HTTPException(status_code=404, detail="Loja não encontrada")
    session.delete(db_store)
    session.commit()
    return {"message": "Loja deletada com sucesso"}
