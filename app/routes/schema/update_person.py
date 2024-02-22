from pydantic import BaseModel, Field
from typing import Optional

class update_person_request(BaseModel):
    name: str = Field(... , description="Person Name", min_length=3,max_length=10)
    age : int = Field(... , description="Person Age")
    email: Optional[str] = Field(None, description="Person Email")