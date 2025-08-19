from typing import Optional, List, Literal
from pydantic import BaseModel, Field, EmailStr, field_validator
import re
from ..definition import AppSection
from ...enums import FieldType, ChipType, ValidationType, ImageQuality, AllowedFileTypes


class BaseAppDefinitionRequest(BaseModel):
    """Base class for app definition requests with common validation"""

    app_id: str = Field(description="Clappia app ID")

    @field_validator("app_id")
    @classmethod
    def validate_app_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()


class GetAppDefinitionRequest(BaseAppDefinitionRequest):
    requesting_user_email_address: EmailStr = Field(
        description="Email of requesting user"
    )
    language: str = Field(default="en", description="Language code")
    strip_html: bool = Field(default=True, description="Remove HTML formatting")
    include_tags: bool = Field(default=True, description="Include metadata tags")


class CreateAppRequest(BaseModel):
    app_name: str = Field(min_length=3, description="Name of the app to create")
    requesting_user_email_address: EmailStr = Field(
        description="Email of requesting user"
    )
    sections: List[AppSection] = Field(
        min_length=1, description="Array of sections with fields"
    )


class AddFieldRequest(BaseAppDefinitionRequest):
    requesting_user_email_address: EmailStr = Field(
        description="Email of user adding field"
    )
    section_index: int = Field(ge=0, description="Section index")
    field_index: int = Field(ge=0, description="Field index")
    field_type: FieldType = Field(
        description="Type of field, possible values are singleLineText, multiLineText, singleSelector, multiSelector, dropDown, dateSelector, timeSelector, phoneNumber, uniqueNumbering, file, gpsLocation, html, calculationsAndLogic, codeScanner, counter, slider, signature, validation, liveTracking, nfcReader, address"
    )
    label: Optional[str] = Field(None, description="Display label")
    description: Optional[str] = Field(None, description="Field description")
    required: Optional[bool] = Field(None, description="Whether field is required")
    block_width_percentage_desktop: Optional[Literal[25, 50, 75, 100]] = Field(
        None, description="Desktop width"
    )
    block_width_percentage_mobile: Optional[Literal[50, 100]] = Field(
        None, description="Mobile width"
    )
    display_condition: Optional[str] = Field(None, description="Display condition")
    retain_values: Optional[bool] = Field(None, description="Retain values when hidden")
    is_editable: Optional[bool] = Field(None, description="Whether field is editable")
    editability_condition: Optional[str] = Field(
        None, description="Editability condition"
    )
    validation: Optional[str] = Field(None, description="Validation type")
    default_value: Optional[str] = Field(None, description="Default value")
    options: Optional[List[str]] = Field(
        None, description="Options for selector fields"
    )
    style: Optional[ChipType] = Field(None, description="Style for selector fields")
    number_of_cols: Optional[int] = Field(None, description="Number of columns")
    allowed_file_types: Optional[List[AllowedFileTypes]] = Field(
        None, description="Allowed file types, for file fields"
    )
    max_file_allowed: Optional[int] = Field(
        None, ge=1, le=10, description="Maximum files"
    )
    image_quality: Optional[ImageQuality] = Field(None, description="Image quality")
    image_text: Optional[str] = Field(None, description="Image text overlay")
    file_name_prefix: Optional[str] = Field(None, description="File name prefix")
    formula: Optional[str] = Field(None, description="Formula for calculation fields")
    hidden: Optional[bool] = Field(None, description="Whether field is hidden")


class UpdateFieldRequest(BaseAppDefinitionRequest):
    requesting_user_email_address: EmailStr = Field(
        description="Email of user updating field"
    )
    field_name: str = Field(description="Variable name of field to update")
    label: Optional[str] = Field(None, description="New display label")
    description: Optional[str] = Field(None, description="New field description")
    required: Optional[bool] = Field(None, description="Whether field is mandatory")
    block_width_percentage_desktop: Optional[Literal[25, 50, 75, 100]] = Field(
        None, description="Desktop width"
    )
    block_width_percentage_mobile: Optional[Literal[50, 100]] = Field(
        None, description="Mobile width"
    )
    display_condition: Optional[str] = Field(None, description="Display condition")
    retain_values: Optional[bool] = Field(None, description="Retain values when hidden")
    is_editable: Optional[bool] = Field(None, description="Whether field is editable")
    editability_condition: Optional[str] = Field(
        None, description="Editability condition"
    )
    validation: Optional[ValidationType] = Field(None, description="Validation type")
    default_value: Optional[str] = Field(None, description="Default value")
    options: Optional[List[str]] = Field(
        None, description="Options for selector fields"
    )
    style: Optional[ChipType] = Field(None, description="Style for selector fields")
    number_of_cols: Optional[int] = Field(None, description="Number of columns")
    allowed_file_types: Optional[List[AllowedFileTypes]] = Field(
        None, description="Allowed file types, for file fields"
    )
    max_file_allowed: Optional[int] = Field(
        None, ge=1, le=10, description="Maximum files"
    )
    image_quality: Optional[ImageQuality] = Field(None, description="Image quality")
    image_text: Optional[str] = Field(None, description="Image text overlay")
    file_name_prefix: Optional[str] = Field(None, description="File name prefix")
    formula: Optional[str] = Field(None, description="Formula for calculation fields")
    hidden: Optional[bool] = Field(None, description="Whether field is hidden")

    @field_validator("field_name")
    @classmethod
    def validate_field_name(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("field_name is required and cannot be empty")
        return v.strip()
