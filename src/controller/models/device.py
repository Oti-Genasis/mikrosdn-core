from pydantic import BaseModel

class Device(BaseModel):
    id: int
    name: str
    ip_address: str
    api_port: int = 8729
    username: str
    password: str