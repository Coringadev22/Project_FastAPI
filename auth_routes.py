from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models import User

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def get_auth():
    return JSONResponse(content={"message": "Voce acessou a rota de autenticacao", "auth": False})


