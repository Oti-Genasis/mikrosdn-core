from fastapi import APIRouter, HTTPException
from models.device import *
from typing import List

router = APIRouter()

# list of devices (in-memory for demonstration)
devices = [
    DeviceFull(id=1, name="Mikrotik RouterOS_1", ip_address="192.168.88.1", username="admin", password="pass", api_port=8729, serial_number="SN123456", device_model="RouterOS", os_version="6.48.1", architecture="MIPSBE", license="Free"),
    DeviceFull(id=2, name="Mikrotik RouterOS_2", ip_address="192.168.88.2", username="admin", password="pass", api_port=8729, serial_number="SN654321", device_model="RouterOS", os_version="6.48.1", architecture="MIPSBE", license="Free"),
    DeviceFull(id=3, name="Mikrotik RouterOS_3", ip_address="192.168.88.3", username="admin", password="pass", api_port=8729, serial_number="SN789012", device_model="RouterOS", os_version="6.48.1", architecture="MIPSBE", license="Free"),
    DeviceFull(id=4, name="Mikrotik RouterOS_4", ip_address="192.168.88.4", username="admin", password="pass", api_port=8729, serial_number="SN345678", device_model="RouterOS", os_version="6.48.1", architecture="MIPSBE", license="Free"),
]

@router.get("/devices", response_model=List[DevicePrint])
def print_devices():
    if not devices:
        raise HTTPException(status_code=404, detail="No devices found")
    return devices

@router.get("/devices/{device_id}", response_model=DevicePrint)
def print_devices(device_id: int):
    for element in devices:
        if element.id == device_id:
            return element
    raise HTTPException(status_code=404, detail="Device not found")

@router.post("/devices", response_model=DeviceAdd)
def add_device(blanck_device: DeviceAdd):
    new_device_id = len(devices) + 1

    new_device = DeviceAdd(id=new_device_id,
                        name = blanck_device.name,
                        ip_address = blanck_device.ip_address,
                        api_port = blanck_device.api_port,
                        username = blanck_device.username,
                        password = blanck_device.password)
    
    devices.append(new_device)

    return new_device

@router.put("/devices/{device_id}", response_model=DeviceUpdate)
def update_device(device_id: int, updated_device: DeviceUpdate):
    for element in devices:
        if element.id == device_id:
            element.name = updated_device.name
            element.ip_address = updated_device.ip_address
            element.api_port = updated_device.api_port
            element.username = updated_device.username
            element.password = updated_device.password
            return element
    return {"error": "Device not found"}, 404

@router.delete("/devices/{device_id}")
def delete_device(device_id: int):
    for i, device in enumerate(devices):
        if device.id == device_id:
            deleted_device = devices.pop(i)
            return deleted_device
    return {"error": "Device not found"}, 404