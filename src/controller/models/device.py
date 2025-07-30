from typing import Optional
from pydantic import BaseModel, Field
from config import *

# Define a complete model for devices
class DeviceFull(BaseModel):
    id: int = Field(..., ge=1, description="Unique identifier for the device")
    name: str = Field(..., min_length=3, max_length=255, description="Name of the device")
    ip_address: str = Field(..., description="IP address of the device")
    api_port: int = Field(ROUTEROS_DEFAULT_API_PORT, ge=1, le=65535, description="API port of the device")
    username: str = Field(ROUTEROS_API_DEFAULT_USERNAME, min_length=3, max_length=64, description="Username for the device")
    password: str = Field(ROUTEROS_API_DEFAULT_PASSWORD, min_length=3, max_length=128, description="Password for the device")
    serial_number: Optional[str] = Field(None, description="Serial number of the device")
    device_model: Optional[str] = Field(None, description="Model of the device")
    os_version: Optional[str] = Field(None, description="Operating system version of the device")
    architecture: Optional[str] = Field(None, description="Architecture of the device")
    license: Optional[str] = Field(None, description="License information of the device")
    

########################################
# Define models for different operations
########################################

class DeviceAdd(BaseModel):
    ip_address: str = Field(..., description="IP address of the device")
    name: str = Field(..., min_length=1, max_length=255, description="Name of the device")
    username: str = Field("admin", min_length=3, max_length=64, description="Username for the device")
    password: str = Field("pass", min_length=3, max_length=128, description="Password for the device")

class DeviceUpdate(BaseModel):
    id: int = Field(..., ge=1, description="Unique identifier for the device")
    ip_address: Optional[str] = Field(None, description="IP address of the device")
    username: Optional[str] = Field(None, min_length=3, max_length=64, description="Username for the device")
    password: Optional[str] = Field(None, min_length=6, max_length=128, description="Password for the device")
    name: Optional[str] = Field(None, min_length=1, max_length=255, description="Name of the device")
    api_port: Optional[int] = Field(ROUTEROS_DEFAULT_API_PORT, ge=1, le=65535, description="API port of the device")

class DeviceDelete(BaseModel):
    pass

class DevicePrint(DeviceFull):
    pass
    

class DeviceConnect(BaseModel):
    pass
