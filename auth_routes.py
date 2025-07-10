from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models import User
from models import Session

session = Session()

# ------------------------------------------------------------ 

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def get_auth():
    users = session.query(User).all()
    return JSONResponse(content={"message": "Voce acessou a rota de autenticacao", "auth": users})


