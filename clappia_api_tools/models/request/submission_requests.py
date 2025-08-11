from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, EmailStr, field_validator
import re
from ..submission import SubmissionFilters, AggregationDimension, AggregationMetric
from ...enums import ExcelFormat

class GetSubmissionsRequest(BaseModel):
    app_id: str = Field(description="The Clappia app ID")
    requesting_user_email_address: EmailStr = Field(description="Email of requesting user")
    page_size: int = Field(default=10, ge=1, le=1000, description="Number of submissions per page")
    forward: bool = Field(default=True, description="Direction for pagination")
    filters: Optional[SubmissionFilters] = Field(None, description="Optional filters")
    
    @field_validator('app_id')
    def validate_app_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()

class GetSubmissionsAggregationRequest(BaseModel):
    app_id: str = Field(description="The Clappia app ID")
    requesting_user_email_address: EmailStr = Field(description="Email of requesting user")
    forward: bool = Field(default=True, description="Direction for pagination")
    dimensions: Optional[List[AggregationDimension]] = Field(None, description="Fields to group by")
    aggregation_dimensions: Optional[List[AggregationMetric]] = Field(None, description="Aggregation calculations")
    x_axis_labels: Optional[List[str]] = Field(None, description="X-axis labels for charts")
    page_size: int = Field(default=1000, ge=1, le=1000, description="Number of results per page")
    filters: Optional[SubmissionFilters] = Field(None, description="Optional filters")
    
    @field_validator('app_id')
    def validate_app_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()

class CreateSubmissionRequest(BaseModel):
    app_id: str = Field(description="The Clappia app ID")
    requesting_user_email_address: EmailStr = Field(description="Email of requesting user")
    data: Dict[str, Any] = Field(description="Submission data, in the format of a dictionary. Example {'employee_name': 'Jane Doe', 'department': 'HR', 'salary': 60000, 'start_date': '10-02-2024', 'location':'23.456789, 45.678901', 'image_field_name': [{\"s3Path\": {\"bucket\": \"my-files-bucket\", \"key\": \"images/photo.jpg\", \"makePublic\": false}}]}")
    
    @field_validator('app_id')
    def validate_app_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()

class EditSubmissionRequest(BaseModel):
    app_id: str = Field(description="The Clappia app ID")
    submission_id: str = Field(description="The submission ID to edit")
    requesting_user_email_address: EmailStr = Field(description="Email of requesting user")
    data: Dict[str, Any] = Field(description="Updated submission data, in the format of a dictionary. Example {'employee_name': 'Jane Doe', 'department': 'HR', 'salary': 60000, 'start_date': '10-02-2024', 'location':'23.456789, 45.678901', 'image_field_name': [{\"s3Path\": {\"bucket\": \"my-files-bucket\", \"key\": \"images/photo.jpg\", \"makePublic\": false}}]}")
    
    @field_validator('app_id')
    def validate_app_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()
    
    @field_validator('submission_id')
    def validate_submission_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Submission ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("Submission ID must contain only uppercase letters and numbers")
        return v.strip()

class UpdateSubmissionStatusRequest(BaseModel):
    app_id: str = Field(description="The Clappia app ID")
    submission_id: str = Field(description="The submission ID")
    requesting_user_email_address: EmailStr = Field(description="Email of requesting user")
    status_name: str = Field(description="New status name")
    comments: Optional[str] = Field(None, description="Optional comments")
    
    @field_validator('app_id')
    def validate_app_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()
    
    @field_validator('submission_id')
    def validate_submission_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Submission ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("Submission ID must contain only uppercase letters and numbers")
        return v.strip()

class UpdateSubmissionOwnersRequest(BaseModel):
    app_id: str = Field(description="The Clappia app ID")
    submission_id: str = Field(description="The submission ID")
    requesting_user_email_address: EmailStr = Field(description="Email of requesting user")
    email_ids: List[EmailStr] = Field(min_length=1, description="List of email addresses")
    
    @field_validator('app_id')
    def validate_app_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()
    
    @field_validator('submission_id')
    def validate_submission_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Submission ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("Submission ID must contain only uppercase letters and numbers")
        return v.strip()

class GetSubmissionsInExcelRequest(BaseModel):
    app_id: str = Field(description="The Clappia app ID")
    requesting_user_email_address: EmailStr = Field(description="Email of requesting user")
    filters: Optional[SubmissionFilters] = Field(None, description="Optional filters")
    field_names: Optional[List[str]] = Field(None, description="List of field names to include in export, both standard and custom fields")
    format: ExcelFormat = Field(default=ExcelFormat.EXCEL, description="Export format")
    
    @field_validator('app_id')
    def validate_app_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip() 