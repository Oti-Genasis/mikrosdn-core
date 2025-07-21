from fastapi import APIRouter
from models.device import Device

router = APIRouter()

# list of devices (in-memory for demonstration)
devices = [
    Device(id=1, name="Mikrotik RouterOS_1", ip_address="192.168.88.1", username="admin", password="pass")
]

@router.get("/devices", response_model=list[Device])
def list_devices():
    return devices