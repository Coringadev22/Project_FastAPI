from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy_utils import ChoiceType

db = create_engine("sqlite:///database.db")

Base = declarative_base()

# ------------------------------ USER ----------------------------------------

class User(Base):
    __tablename__ = "users"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    email = Column("email", String, unique=True, nullable=False)
    password = Column("password", String, nullable=False)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, default=datetime.now(), onupdate=datetime.now())
    orders = relationship("Order", back_populates="user")
    active = Column("active", Boolean, default=True)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, name, email, password, admin=False, active=True):
        self.name = name
        self.email = email
        self.password = password
        self.admin = admin
        self.active = active
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

# ------------------------------ ORDER -------------------------------------



class Order(Base):
    __tablename__ = "orders"

    # STATUS_ORDER = [
    #     ("PENDING", "pending"),
    #     ("PAID", "paid"),
    #     ("CANCELLED", "cancelled"),
    #     ("SHIPPED", "shipped"),
    #     ("DELIVERED", "delivered"),
    # ]


    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String, nullable=False, default="pending")
    user = Column("user", ForeignKey("users.id"), nullable=False)
    price = Column("price", Float, nullable=False)
    
    def __init__(self, status, user, price):
        self.status = status
        self.user = user
        self.price = price



# ------------------------------ ITEMS ORDER ---------------------------------



class Items_Order(Base):
    __tablename__ = "items_order"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    order = Column("order", ForeignKey("orders.id"), nullable=False)
    quantity = Column("quantity", Integer, nullable=False)
    tamanho = Column("tamanho", String, nullable=False)
    unity_price = Column("unity_price", Float, nullable=False)
    types_pizza = Column("types_pizza", String, nullable=False)
    
    
    def __init__(self, order, quantity, tamanho, unity_price, types_pizza):
        self.order = order
        self.quantity = quantity
        self.tamanho = tamanho
        self.unity_price = unity_price
        self.types_pizza = types_pizza
        
        
        