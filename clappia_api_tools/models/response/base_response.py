from typing import Optional, Any
from pydantic import BaseModel, Field

class BaseResponse(BaseModel):
    success: bool = Field(description="Whether operation was successful")
    message: str = Field(description="Response message")
    data: Optional[Any] = Field(None, description="Response data") 