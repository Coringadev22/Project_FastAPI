# uvicorn main:app --reload

# ------------------------------------------------------------ 

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
    
# ------------------------------------------------------------ 

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)

