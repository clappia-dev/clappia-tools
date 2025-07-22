from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class BaseResponse(BaseModel):
    success: bool = Field(description="Whether operation was successful")
    message: str = Field(description="Response message")
    data: Optional[Any] = Field(None, description="Response data")

class AppDefinitionResponse(BaseResponse):
    app_id: str = Field(None, description="App ID")

class AppCreationResponse(BaseResponse):
    app_id: str = Field(None, description="Generated app ID")
    app_name: Optional[str] = Field(None, description="Name of created app")
    sections_created: Optional[int] = Field(None, description="Number of sections created")

class SubmissionResponse(BaseResponse):
    app_id: str = Field(None, description="App ID")
    submission_id: Optional[str] = Field(None, description="Submission ID")
    operation: str = Field(description="Type of operation performed")

class SubmissionsResponse(BaseResponse):
    app_id: str = Field(None, description="App ID")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Metadata")

class SubmissionsAggregationResponse(BaseResponse):
    app_id: str = Field(None, description="App ID")

class FieldOperationResponse(BaseResponse):
    app_id: str = Field(description="App ID where field was modified")
    field_name: Optional[str] = Field(None, description="Name of the field")
    operation: str = Field(description="Type of operation performed")

class SubmissionsExcelResponse(BaseResponse):
    app_id: str = Field(None, description="App ID")
    url: Optional[str] = Field(None, description="Download URL for the exported file")
    format: Optional[str] = Field(None, description="Export format used")
    requesting_user_email_address: Optional[str] = Field(None, description="Email address where file was sent")