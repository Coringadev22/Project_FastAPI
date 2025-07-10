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
from users import user_router
from delivery_man import delivery_man_router
from motocycle import motocycle_router
from store import store_router
app.include_router(auth_router)
app.include_router(order_router)
app.include_router(user_router)
app.include_router(delivery_man_router)
app.include_router(motocycle_router)
app.include_router(store_router)
# ------------------------------------------------------------------
# Allow running the API with `python main.py` or `python main.py runserver`
# ------------------------------------------------------------------

if __name__ == "__main__":
    import uvicorn, sys

    # Accept optional host:port and reload flag via CLI or default values
    host = "127.0.0.1"
    port = 8000
    reload = True

    # Usage examples:
    #   python main.py               -> starts at 127.0.0.1:8000 with reload
    #   python main.py 0.0.0.0 9000  -> custom host/port
    #   python main.py noreload      -> disable reload
    #   python main.py runserver     -> alias for default behaviour

    args = sys.argv[1:]
    if args:
        if args[0] == "noreload":
            reload = False
        elif args[0] == "runserver":
            pass  # keep defaults
        else:
            host = args[0]
            if len(args) > 1 and args[1].isdigit():
                port = int(args[1])
            if len(args) > 2 and args[2] == "noreload":
                reload = False

    uvicorn.run("main:app", host=host, port=port, reload=reload)

