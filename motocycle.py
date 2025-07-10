from fastapi import APIRouter, HTTPException
from typing import List, Optional
from pydantic import BaseModel
from models import Session, Motocycle

motocycle_router = APIRouter(prefix="/motocycle", tags=["motocycle"])
session = Session()

class MotocycleCreate(BaseModel):
    brand: str
    model: str
    year: int
    color: str
    plate: str
    km_start: int
    km_end: int
    delivery_man: int
    active: Optional[bool] = True

class MotocycleUpdate(BaseModel):
    brand: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None
    color: Optional[str] = None
    plate: Optional[str] = None
    km_start: Optional[int] = None
    km_end: Optional[int] = None
    delivery_man: Optional[int] = None
    active: Optional[bool] = None

@motocycle_router.get("/", response_model=List[dict])
async def get_motocycles():
    motocycles = session.query(Motocycle).all()
    result = []
    for m in motocycles:
        result.append({
            "id": m.id,
            "brand": m.brand,
            "model": m.model,
            "year": m.year,
            "color": m.color,
            "plate": m.plate,
            "km_start": m.km_start,
            "km_end": m.km_end,
            "delivery_man": m.delivery_man,
            "active": m.active,
            "created_at": m.created_at,
            "updated_at": m.updated_at
        })
    return result

@motocycle_router.get("/{motocycle_id}", response_model=dict)
async def get_motocycle(motocycle_id: int):
    m = session.query(Motocycle).filter(Motocycle.id == motocycle_id).first()
    if not m:
        raise HTTPException(status_code=404, detail="Motocicleta não encontrada")
    return {
        "id": m.id,
        "brand": m.brand,
        "model": m.model,
        "year": m.year,
        "color": m.color,
        "plate": m.plate,
        "km_start": m.km_start,
        "km_end": m.km_end,
        "delivery_man": m.delivery_man,
        "active": m.active,
        "created_at": m.created_at,
        "updated_at": m.updated_at
    }

@motocycle_router.post("/", response_model=dict)
async def create_motocycle(motocycle: MotocycleCreate):
    db_motocycle = Motocycle(
        brand=motocycle.brand,
        model=motocycle.model,
        year=motocycle.year,
        color=motocycle.color,
        plate=motocycle.plate,
        km_start=motocycle.km_start,
        km_end=motocycle.km_end,
        delivery_man=motocycle.delivery_man,
        active=motocycle.active
    )
    session.add(db_motocycle)
    session.commit()
    session.refresh(db_motocycle)
    return {
        "id": db_motocycle.id,
        "brand": db_motocycle.brand,
        "model": db_motocycle.model,
        "year": db_motocycle.year,
        "color": db_motocycle.color,
        "plate": db_motocycle.plate,
        "km_start": db_motocycle.km_start,
        "km_end": db_motocycle.km_end,
        "delivery_man": db_motocycle.delivery_man,
        "active": db_motocycle.active,
        "created_at": db_motocycle.created_at,
        "updated_at": db_motocycle.updated_at
    }

@motocycle_router.put("/{motocycle_id}", response_model=dict)
async def update_motocycle(motocycle_id: int, motocycle: MotocycleUpdate):
    db_motocycle = session.query(Motocycle).filter(Motocycle.id == motocycle_id).first()
    if not db_motocycle:
        raise HTTPException(status_code=404, detail="Motocicleta não encontrada")
    if motocycle.brand is not None:
        db_motocycle.brand = motocycle.brand
    if motocycle.model is not None:
        db_motocycle.model = motocycle.model
    if motocycle.year is not None:
        db_motocycle.year = motocycle.year
    if motocycle.color is not None:
        db_motocycle.color = motocycle.color
    if motocycle.plate is not None:
        db_motocycle.plate = motocycle.plate
    if motocycle.km_start is not None:
        db_motocycle.km_start = motocycle.km_start
    if motocycle.km_end is not None:
        db_motocycle.km_end = motocycle.km_end
    if motocycle.delivery_man is not None:
        db_motocycle.delivery_man = motocycle.delivery_man
    if motocycle.active is not None:
        db_motocycle.active = motocycle.active
    session.commit()
    session.refresh(db_motocycle)
    return {
        "id": db_motocycle.id,
        "brand": db_motocycle.brand,
        "model": db_motocycle.model,
        "year": db_motocycle.year,
        "color": db_motocycle.color,
        "plate": db_motocycle.plate,
        "km_start": db_motocycle.km_start,
        "km_end": db_motocycle.km_end,
        "delivery_man": db_motocycle.delivery_man,
        "active": db_motocycle.active,
        "created_at": db_motocycle.created_at,
        "updated_at": db_motocycle.updated_at
    }

@motocycle_router.delete("/{motocycle_id}", response_model=dict)
async def delete_motocycle(motocycle_id: int):
    db_motocycle = session.query(Motocycle).filter(Motocycle.id == motocycle_id).first()
    if not db_motocycle:
        raise HTTPException(status_code=404, detail="Motocicleta não encontrada")
    session.delete(db_motocycle)
    session.commit()
    return {"message": "Motocicleta deletada com sucesso"}
