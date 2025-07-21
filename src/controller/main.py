from fastapi import FastAPI
from routers.devices import router as devices_router


app = FastAPI(
    title="MikroSDN API",
    description="Backend API for managing MikroTik devices",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to MikroSDN API"}

app.include_router(devices_router)