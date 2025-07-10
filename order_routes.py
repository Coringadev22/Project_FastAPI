from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models import Order, Items_Order, Customer, Delivery_Man, Store, Motocycle, User, Session
from schemas import OrderCreate


# SQLAlchemy session
session = Session()


order_router = APIRouter(prefix="/orders", tags=["orders"])

@order_router.get("/")
async def get_orders():
    orders = session.query(Order).all()
    return JSONResponse(content={"message": "Voce acessou a rota de pedidos", "orders": orders})
    


@order_router.post("/", response_model=dict)
async def create_order(order: OrderCreate):
    db_order = Order(
        status=order.status,
        user=order.user,
        price=order.price,
        customer=order.customer,
        delivery_man=order.delivery_man,
        store=order.store,
        items_order=order.items_order,
        payment_method=order.payment_method,
    )
    session.add(db_order)
    session.commit()
    session.refresh(db_order)
    return {"message": "Pedido criado com sucesso"}


@order_router.put("/{order_id}", response_model=dict)
async def update_order(order_id: int, order: OrderCreate):
    db_order = session.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        return JSONResponse(status_code=404, content={"message": "Pedido nao encontrado"})
    db_order.status = order.status
    db_order.user = order.user
    db_order.price = order.price
    db_order.customer = order.customer
    db_order.delivery_man = order.delivery_man
    db_order.store = order.store
    db_order.payment_method = order.payment_method
    db_order.items_order = order.items_order
    session.commit()
    return {"message": "Pedido atualizado com sucesso"}


@order_router.delete("/{order_id}", response_model=dict)
async def delete_order(order_id: int):
    db_order = session.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        return JSONResponse(status_code=404, content={"message": "Pedido nao encontrado"})
    session.delete(db_order)
    session.commit()
    return {"message": "Pedido deletado com sucesso"} 



