from pydantic import BaseModel
from typing import List

class Config(BaseModel):
    welcome: str = ""
    send_message: List[str] = []

