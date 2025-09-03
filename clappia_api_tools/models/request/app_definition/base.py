from typing import Optional, List, Literal, Dict, Any
from pydantic import BaseModel, Field, ConfigDict, field_validator
import re
import json
from urllib.parse import urlparse


class JsonSerializableMixin:
    """Mixin to provide common JSON serialization functionality"""
    
    def to_json(self) -> Dict[str, Any]:
        data = {}
        for field_name, field_value in self.__dict__.items():
            if field_value is not None:
                camel_case_key = self._to_camel_case(field_name)
                if hasattr(field_value, 'to_json'):
                    data[camel_case_key] = field_value.to_json()
                elif isinstance(field_value, list) and all(hasattr(item, 'to_json') for item in field_value):
                    data[camel_case_key] = [item.to_json() for item in field_value]
                else:
                    data[camel_case_key] = field_value
        return data
    
    @staticmethod
    def _to_camel_case(snake_str: str) -> str:
        components = snake_str.split('_')
        return components[0] + ''.join(word.capitalize() for word in components[1:])


class ValidatedString(str):
    """Custom string type with common validation patterns"""
    
    @classmethod
    def field_name_validator(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            if not v or not v.strip():
                raise ValueError("Field name cannot be empty")
            v = v.strip()
            if not re.match(r"^[_a-z][\d_a-z]*$", v):
                raise ValueError("Field name must start with letter/underscore and contain only lowercase letters, numbers, underscore")
        return v
    
    @classmethod
    def non_empty_string_validator(cls, v: Optional[str], field_name: str = "Field") -> Optional[str]:
        if v is not None and (not v or not v.strip()):
            raise ValueError(f"{field_name} cannot be empty")
        return v.strip() if v else v
    
    @classmethod
    def url_validator(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("URL is required")
        v = v.strip()
        try:
            result = urlparse(v)
            if not all([result.scheme, result.netloc]):
                raise ValueError("Must be a valid URL")
        except Exception:
            raise ValueError("Must be a valid URL")
        return v
    
    @classmethod
    def json_string_validator(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            try:
                json.loads(v)
            except json.JSONDecodeError:
                raise ValueError("Must be valid JSON string")
        return v


class UniqueListValidator:
    """Validator for ensuring list uniqueness"""
    
    @classmethod
    def validate_unique_strings(cls, v: Optional[List[str]], field_name: str = "Items") -> Optional[List[str]]:
        if v is not None:
            if len(set(v)) != len(v):
                raise ValueError(f"{field_name} must be unique")
            for item in v:
                if not item or not item.strip():
                    raise ValueError(f"{field_name} cannot contain empty values")
        return v


class BaseFieldComponent(BaseModel, JsonSerializableMixin):
    """Base component for field-related models"""
    model_config = ConfigDict(str_strip_whitespace=True, validate_assignment=True)


# Field type enum
FieldTypeEnum = Literal[
    "singleLineText", "multiLineText", "richTextEditor", "numberInput", "urlInput", "emailInput",
    "dropDown", "singleSelector", "multiSelector", "tags", "dateSelector", "timeSelector",
    "codeScanner", "nfcReader", "ratings", "toggle", "range", "counter", "slider",
    "phoneNumber", "address", "geoAddress", "paymentGateway", "file", "audio",
    "gpsLocation", "liveTracking", "signature", "calculationsAndLogic", "uniqueNumbering",
    "getDataFromOtherApps", "getDataFromRestApis", "getDataFromDatabase", "ai",
    "html", "attachedFiles", "imageViewer", "videoViewer", "pdfViewer", "progressBar",
    "validation", "button", "code"
]


# Base request class - this would need to be imported from the parent directory
# For now, we'll define a placeholder that can be updated later
class BaseAppDefinitionRequest(BaseModel):
    """Base class for app definition requests - placeholder for now"""
    pass


class BaseAddFieldRequest(BaseAppDefinitionRequest, JsonSerializableMixin):
    model_config = ConfigDict(str_strip_whitespace=True, validate_assignment=True)
    app_id: str = Field(description="App ID, must be a valid Clappia app ID")
    page_index: int = Field(ge=0, description="Page index, must be a valid page index and greater than or equal to 0")
    section_index: int = Field(ge=0, description="Section index, must be a valid section index and greater than or equal to 0")
    field_index: int = Field(ge=0, description="Field index, must be a valid field index and greater than or equal to 0")
    field_type: FieldTypeEnum = Field(description="Type of field to add")
    field_name: str = Field(description="Field name, should be a valid field name and should be unique")
    label: str = Field(description="Display label for the field")
    description: Optional[str] = Field(None, description="Field description, Example: This is a description for the field")
    placeholder: Optional[str] = Field(None, description="Field placeholder")
    dependency_app_id: Optional[str] = Field(None, description="Dependency app ID, must be a valid Clappia app ID, mandatory if dependency_type is getDataFromOtherApps")
    server_url: Optional[str] = Field(None, description="Server URL, mandatory if field type is getDataFromRestApis")
    display_condition: Optional[str] = Field(None, description="Display condition Example: {field_name} == 'value'")
    required: bool = Field(default=False, description="Whether field is required")
    hidden: bool = Field(default=False, description="Whether field is hidden")
    is_editable: bool = Field(default=True, description="Whether field is editable")
    editability_condition: Optional[str] = Field(None, description="Editability condition, Example: {field_name} == 'value'")
    default_value: Optional[str] = Field(None, description="Default value, Example: 'value'")
    width: int = Field(default=100, description="Desktop width")
    mobile_width: int = Field(default=100, description="Mobile width")
    retain_values: bool = Field(default=True, description="Retain values when hidden")

    @field_validator("field_name")
    @classmethod
    def validate_field_names(cls, v: Optional[str]) -> Optional[str]:
        return ValidatedString.field_name_validator(v)

    @field_validator("label")
    @classmethod
    def validate_label(cls, v: str) -> str:
        return ValidatedString.non_empty_string_validator(v, "Label")
