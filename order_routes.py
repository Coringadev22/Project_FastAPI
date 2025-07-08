from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models import Order, Items_Order

order_router = APIRouter(prefix="/orders", tags=["orders"])

@order_router.get("/")
async def get_orders():
    return JSONResponse(content={"message": "Voce acessou a rota de pedidos"})
    




