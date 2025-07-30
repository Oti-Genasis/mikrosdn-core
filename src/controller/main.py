from fastapi import FastAPI
from routers.devices import router as devices_endpoint


app = FastAPI(
    title="MikroSDN API",
    description="Backend API for managing MikroTik devices",
    version="0.1.0"
)

app.include_router(devices_endpoint)