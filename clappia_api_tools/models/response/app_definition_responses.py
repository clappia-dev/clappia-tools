from typing import Optional
from pydantic import BaseModel, Field
from .base_response import BaseResponse

class AppDefinitionResponse(BaseResponse):
    app_id: str = Field(None, description="App ID")

class AppCreationResponse(BaseResponse):
    app_id: str = Field(None, description="Generated app ID")
    app_name: Optional[str] = Field(None, description="Name of created app")
    sections_created: Optional[int] = Field(None, description="Number of sections created")

class FieldOperationResponse(BaseResponse):
    app_id: str = Field(description="App ID where field was modified")
    field_name: Optional[str] = Field(None, description="Name of the field")
    operation: str = Field(description="Type of operation performed")