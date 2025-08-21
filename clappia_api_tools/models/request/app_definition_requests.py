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


class AddSectionRequest(BaseAppDefinitionRequest):
    requesting_user_email_address: EmailStr = Field(
        description="Email of user adding section"
    )
    section_index: int = Field(ge=0, description="Position where section will be inserted (0-based)")
    page_index: int = Field(ge=0, description="Page index where section will be added")
    section_name: str = Field(description="Display name for the section")
    description: Optional[str] = Field(None, description="Optional help text for the section")
    is_collapsible: Optional[bool] = Field(None, description="Allow users to expand/collapse section")
    is_collapsed_by_default: Optional[bool] = Field(None, description="Initial collapsed state")


class UpdateSectionRequest(BaseAppDefinitionRequest):
    requesting_user_email_address: EmailStr = Field(
        description="Email of user updating section"
    )
    section_index: int = Field(ge=0, description="Index of the section to update")
    page_index: int = Field(ge=0, description="Page index of the section")
    section_name: Optional[str] = Field(None, description="Display title of the section")
    description: Optional[str] = Field(None, description="Help text or instructions for the section")
    is_collapsible: Optional[bool] = Field(None, description="Enable/disable expand/collapse functionality")
    is_collapsed_by_default: Optional[bool] = Field(None, description="Set initial display state")
    keep_section_collapsed: Optional[bool] = Field(None, description="Keep section collapsed")
    allow_copy: Optional[bool] = Field(None, description="Allow copying of the section")
    max_number_of_copies: Optional[int] = Field(None, ge=1, description="Maximum number of copies allowed")
    add_section_text: Optional[str] = Field(None, description="Text for add section button")
    display_condition: Optional[str] = Field(None, description="Display condition for the section")


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


class RemovePageBreakRequest(BaseAppDefinitionRequest):
    requesting_user_email_address: EmailStr = Field(
        description="Email of requesting user"
    )
    page_index: int = Field(ge=0, description="Page index to remove")

    @field_validator("page_index")
    @classmethod
    def validate_page_index(cls, v: int) -> int:
        if v < 0:
            raise ValueError("Page index cannot be negative")
        return v


class AddPageBreakRequest(BaseAppDefinitionRequest):
    requesting_user_email_address: EmailStr = Field(
        description="Email of requesting user"
    )
    page_index: int = Field(ge=0, description="Page index where to add page break")
    section_index: int = Field(ge=0, description="Section index where to add page break")


class UpdatePageBreakRequest(BaseAppDefinitionRequest):
    requesting_user_email_address: EmailStr = Field(
        description="Email of requesting user"
    )
    page_index: int = Field(ge=0, description="Page index to update")
    show_submit_button: Optional[bool] = Field(None, description="Show submit button")
    previous_button_text: Optional[str] = Field(None, description="Previous button text")
    next_button_text: Optional[str] = Field(None, description="Next button text")

    @field_validator("previous_button_text")
    @classmethod
    def validate_previous_button_text(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and v.strip() == "":
            raise ValueError("previous_button_text should not be blank")
        return v.strip() if v else v

    @field_validator("next_button_text")
    @classmethod
    def validate_next_button_text(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and v.strip() == "":
            raise ValueError("next_button_text should not be blank")
        return v.strip() if v else v

    @field_validator("show_submit_button", "previous_button_text", "next_button_text", mode="before")
    @classmethod
    def validate_at_least_one_parameter(cls, values):
        show_submit_button = values.get("show_submit_button")
        previous_button_text = values.get("previous_button_text")
        next_button_text = values.get("next_button_text")
        
        if show_submit_button is None and previous_button_text is None and next_button_text is None:
            raise ValueError("At least one of the parameters 'show_submit_button', 'previous_button_text', or 'next_button_text' is required")
        return values


class ReorderSectionRequest(BaseAppDefinitionRequest):
    requesting_user_email_address: EmailStr = Field(
        description="Email of requesting user"
    )
    source_section_index: int = Field(ge=0, description="Source section index")
    target_section_index: int = Field(ge=0, description="Target section index")
    source_page_index: Optional[int] = Field(None, ge=0, description="Source page index")
    target_page_index: Optional[int] = Field(None, ge=0, description="Target page index")
