from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, EmailStr, validator
import re
from .definition import AppSection
from .submission import SubmissionFilters, AggregationDimension, AggregationMetric

class GetAppDefinitionRequest(BaseModel):
    app_id: str = Field(description="Application identifier")
    requesting_user_email_address: EmailStr = Field(description="Email of requesting user")
    language: str = Field(default="en", description="Language code")
    strip_html: bool = Field(default=True, description="Remove HTML formatting")
    include_tags: bool = Field(default=True, description="Include metadata tags")
    
    @validator('app_id')
    def validate_app_id(cls, v):
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()

class CreateAppRequest(BaseModel):
    app_name: str = Field(min_length=3, description="Name of the app to create")
    requesting_user_email_address: EmailStr = Field(description="Email of requesting user")
    sections: List[AppSection] = Field(min_items=1, description="Array of sections with fields")

class GetSubmissionsRequest(BaseModel):
    app_id: str = Field(description="The Clappia app ID")
    requesting_user_email_address: EmailStr = Field(description="Email of requesting user")
    page_size: int = Field(default=10, ge=1, le=1000, description="Number of submissions per page")
    forward: bool = Field(default=True, description="Direction for pagination")
    filters: Optional[SubmissionFilters] = Field(None, description="Optional filters")
    
    @validator('app_id')
    def validate_app_id(cls, v):
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
    
    @validator('app_id')
    def validate_app_id(cls, v):
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()

class CreateSubmissionRequest(BaseModel):
    app_id: str = Field(description="The Clappia app ID")
    requesting_user_email_address: EmailStr = Field(description="Email of requesting user")
    data: Dict[str, Any] = Field(description="Submission data")
    
    @validator('app_id')
    def validate_app_id(cls, v):
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()

class EditSubmissionRequest(BaseModel):
    app_id: str = Field(description="The Clappia app ID")
    submission_id: str = Field(description="The submission ID to edit")
    requesting_user_email_address: EmailStr = Field(description="Email of requesting user")
    data: Dict[str, Any] = Field(description="Updated submission data")
    
    @validator('app_id')
    def validate_app_id(cls, v):
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()
    
    @validator('submission_id')
    def validate_submission_id(cls, v):
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
    
    @validator('app_id')
    def validate_app_id(cls, v):
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()
    
    @validator('submission_id')
    def validate_submission_id(cls, v):
        if not v or not v.strip():
            raise ValueError("Submission ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("Submission ID must contain only uppercase letters and numbers")
        return v.strip()

class UpdateSubmissionOwnersRequest(BaseModel):
    app_id: str = Field(description="The Clappia app ID")
    submission_id: str = Field(description="The submission ID")
    requesting_user_email_address: EmailStr = Field(description="Email of requesting user")
    email_ids: List[EmailStr] = Field(min_items=1, description="List of email addresses")
    
    @validator('app_id')
    def validate_app_id(cls, v):
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()
    
    @validator('submission_id')
    def validate_submission_id(cls, v):
        if not v or not v.strip():
            raise ValueError("Submission ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("Submission ID must contain only uppercase letters and numbers")
        return v.strip()

class AddFieldRequest(BaseModel):
    app_id: str = Field(description="Application ID")
    requesting_user_email_address: EmailStr = Field(description="Email of user adding field")
    section_index: int = Field(ge=0, description="Section index")
    field_index: int = Field(ge=0, description="Field index")
    field_type: str = Field(
        description="Type of field",
        enum=[
            "singleLineText", "multiLineText", "singleSelector", "multiSelector",
            "dropDown", "dateSelector", "timeSelector", "phoneNumber", "uniqueNumbering",
            "file", "gpsLocation", "html", "calculationsAndLogic", "codeScanner",
            "counter", "slider", "signature", "validation", "liveTracking",
            "nfcReader", "address"
        ]
    )
    label: Optional[str] = Field(None, description="Display label")
    description: Optional[str] = Field(None, description="Field description")
    required: Optional[bool] = Field(None, description="Whether field is required")
    block_width_percentage_desktop: Optional[int] = Field(None, description="Desktop width", enum=[25, 50, 75, 100])
    block_width_percentage_mobile: Optional[int] = Field(None, description="Mobile width", enum=[50, 100])
    display_condition: Optional[str] = Field(None, description="Display condition")
    retain_values: Optional[bool] = Field(None, description="Retain values when hidden")
    is_editable: Optional[bool] = Field(None, description="Whether field is editable")
    editability_condition: Optional[str] = Field(None, description="Editability condition")
    validation: Optional[str] = Field(None, description="Validation type")
    default_value: Optional[str] = Field(None, description="Default value")
    options: Optional[List[str]] = Field(None, description="Options for selector fields")
    style: Optional[str] = Field(None, description="Style for selector fields", enum=["Standard", "Chips"])
    number_of_cols: Optional[int] = Field(None, description="Number of columns")
    allowed_file_types: Optional[List[str]] = Field(None, description="Allowed file types, for file fields", enum=["images_camera_upload", "images_gallery_upload", "videos", "documents"])
    max_file_allowed: Optional[int] = Field(None, ge=1, le=10, description="Maximum files")
    image_quality: Optional[str] = Field(None, description="Image quality", enum=["low", "medium", "high"])
    image_text: Optional[str] = Field(None, description="Image text overlay")
    file_name_prefix: Optional[str] = Field(None, description="File name prefix")
    formula: Optional[str] = Field(None, description="Formula for calculation fields")
    hidden: Optional[bool] = Field(None, description="Whether field is hidden")
    
    @validator('app_id')
    def validate_app_id(cls, v):
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()

class UpdateFieldRequest(BaseModel):
    app_id: str = Field(description="Application ID")
    requesting_user_email_address: EmailStr = Field(description="Email of user updating field")
    field_name: str = Field(description="Variable name of field to update")
    label: Optional[str] = Field(None, description="New display label")
    description: Optional[str] = Field(None, description="New field description")
    required: Optional[bool] = Field(None, description="Whether field is mandatory")
    block_width_percentage_desktop: Optional[int] = Field(None, description="Desktop width", enum=[25, 50, 75, 100])
    block_width_percentage_mobile: Optional[int] = Field(None, description="Mobile width", enum=[50, 100])
    display_condition: Optional[str] = Field(None, description="Display condition")
    retain_values: Optional[bool] = Field(None, description="Retain values when hidden")
    is_editable: Optional[bool] = Field(None, description="Whether field is editable")
    editability_condition: Optional[str] = Field(None, description="Editability condition")
    validation: Optional[str] = Field(None, description="Validation type", enum=["none", "number", "email", "url", "custom"])
    default_value: Optional[str] = Field(None, description="Default value")
    options: Optional[List[str]] = Field(None, description="Options for selector fields")
    style: Optional[str] = Field(None, description="Style for selector fields", enum=["Standard", "Chips"])
    number_of_cols: Optional[int] = Field(None, description="Number of columns")
    allowed_file_types: Optional[List[str]] = Field(None, description="Allowed file types, for file fields", enum=["images_camera_upload", "images_gallery_upload", "videos", "documents"])
    max_file_allowed: Optional[int] = Field(None, ge=1, le=10, description="Maximum files")
    image_quality: Optional[str] = Field(None, description="Image quality", enum=["low", "medium", "high"])
    image_text: Optional[str] = Field(None, description="Image text overlay")
    file_name_prefix: Optional[str] = Field(None, description="File name prefix")
    formula: Optional[str] = Field(None, description="Formula for calculation fields")
    hidden: Optional[bool] = Field(None, description="Whether field is hidden")
    
    @validator('app_id')
    def validate_app_id(cls, v):
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()
    
    @validator('field_name')
    def validate_field_name(cls, v):
        if not v or not v.strip():
            raise ValueError("field_name is required and cannot be empty")
        return v.strip()

class GetSubmissionsInExcelRequest(BaseModel):
    app_id: str = Field(description="The Clappia app ID")
    requesting_user_email_address: EmailStr = Field(description="Email of requesting user")
    filters: Optional[SubmissionFilters] = Field(None, description="Optional filters")
    field_names: Optional[List[str]] = Field(None, description="List of field names to include in export, both standard and custom fields")
    format: str = Field(default="Excel", description="Export format", enum=["Excel", "Csv"])
    
    @validator('app_id')
    def validate_app_id(cls, v):
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()