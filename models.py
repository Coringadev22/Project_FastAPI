from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, default=datetime.now(), onupdate=datetime.now())
    customer = Column("customer", ForeignKey("customer.id"), nullable=False)
    delivery_man = Column("delivery_man", ForeignKey("delivery_man.id"), nullable=False)
    store = Column("store", ForeignKey("store.id"), nullable=False)
    items_order = relationship("Items_Order", back_populates="order")
    active = Column("active", Boolean, default=True)
    payment_method = Column("payment_method", String, nullable=False)
    
    
    def __init__(self, status, user, price, customer, delivery_man, store, payment_method, items_order=None, active_val=True, created_at=None, updated_at=None):
        self.status = status
        self.user = user
        self.price = price
        self.customer = customer
        self.delivery_man = delivery_man
        self.store = store
        self.payment_method = payment_method
        self.items_order = items_order or []
        self.active = active_val
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()



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
        
        
        
# ------------------------------ delivery_man ----------------------------------------

class Delivery_Man(Base):
    __tablename__ = "delivery_man"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    cpf = Column("cpf", String, unique=True, nullable=False)
    phone = Column("phone", String, nullable=False)
    address = Column("address", String, nullable=False)
    number = Column("number", String, nullable=False)
    complement = Column("complement", String, nullable=False)
    neighborhood = Column("neighborhood", String, nullable=False)
    city = Column("city", String, nullable=False)
    state = Column("state", String, nullable=False)
    zip_code = Column("zip_code", String, nullable=False)
    email = Column("email", String, unique=True, nullable=False)
    password = Column("password", String, nullable=False)
    cnh = Column("cnh", String, nullable=False)
    cnh_expiration = Column("cnh_expiration", DateTime, nullable=False)
    cnh_front = Column("cnh_front", String, nullable=False)
    cnh_back = Column("cnh_back", String, nullable=False)
    cnh_photo = Column("cnh_photo", String, nullable=False)
    cnh_photo_back = Column("cnh_photo_back", String, nullable=False)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, default=datetime.now(), onupdate=datetime.now())
    active = Column("active", Boolean, default=True)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, name, email, password, admin=False, active=True):
        self.name = name
        self.email = email
        self.password = password
        self.admin = admin
        self.active = active
        self.created_at = datetime.now()



# ------------------------------ Motocycle ----------------------------------------

class Motocycle(Base):
    __tablename__ = "motocycle"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    brand = Column("brand", String, nullable=False)
    model = Column("model", String, nullable=False)
    year = Column("year", Integer, nullable=False)
    color = Column("color", String, nullable=False)
    plate = Column("plate", String, nullable=False) 
    km_start = Column("km_start", Integer, nullable=False)
    km_end = Column("km_end", Integer, nullable=False)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, default=datetime.now(), onupdate=datetime.now())
    active = Column("active", Boolean, default=True)
    delivery_man = Column("delivery_man", ForeignKey("delivery_man.id"), nullable=False)
    
    def __init__(self, brand, model, year, color, plate, km_start, km_end, delivery_man, active=True):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.plate = plate
        self.km_start = km_start
        self.km_end = km_end
        self.delivery_man = delivery_man
        self.active = active


# ------------------------------ Customer ----------------------------------------



class Customer(Base):
    __tablename__ = "customer"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    phone = Column("phone", String, nullable=False)
    address = Column("address", String, nullable=False)
    number = Column("number", String, nullable=False)
    complement = Column("complement", String, nullable=False)
    neighborhood = Column("neighborhood", String, nullable=False)
    city = Column("city", String, nullable=False)
    state = Column("state", String, nullable=False)
    zip_code = Column("zip_code", String, nullable=False)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, default=datetime.now(), onupdate=datetime.now())
    active = Column("active", Boolean, default=True)

    def __init__(self, name, phone, address, number, complement, neighborhood, city, state, zip_code, active=True):
        self.name = name
        self.phone = phone
        self.address = address
        self.number = number
        self.complement = complement
        self.neighborhood = neighborhood
        self.city = city
        self.state = state
        self.zip_code = zip_code

#-------------------------------- Store ----------------------------------------


class Store(Base):
    __tablename__ = "store"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    phone = Column("phone", String, nullable=False)
    address = Column("address", String, nullable=False)
    number = Column("number", String, nullable=False)
    complement = Column("complement", String, nullable=False)
    neighborhood = Column("neighborhood", String, nullable=False)
    city = Column("city", String, nullable=False)
    state = Column("state", String, nullable=False)
    zip_code = Column("zip_code", String, nullable=False)
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, default=datetime.now(), onupdate=datetime.now())
    active = Column("active", Boolean, default=True)

    def __init__(self, name, phone, address, number, complement, neighborhood, city, state, zip_code, active=True):
        self.name = name
        self.phone = phone
        self.address = address
        self.number = number
        self.complement = complement
        self.neighborhood = neighborhood
        self.city = city
        self.state = state
        self.zip_code = zip_code

Session = sessionmaker(bind=db)