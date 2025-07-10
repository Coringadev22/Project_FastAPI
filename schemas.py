from pydantic import BaseModel
from typing import List, Optional

class OrderItem(BaseModel):
    quantity: int
    tamanho: str
    unity_price: float
    types_pizza: str

class OrderCreate(BaseModel):
    status: str
    user: int
    price: float
    customer: int
    delivery_man: int
    store: int
    payment_method: str
    items_order: Optional[List[OrderItem]] = None 