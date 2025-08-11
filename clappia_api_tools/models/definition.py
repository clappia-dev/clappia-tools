from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, EmailStr, field_validator, ValidationInfo
import re
from ..enums import FieldType

class AppField(BaseModel):
    field_type: FieldType = Field(
        description="Type of field, possible values are singleLineText, multiLineText, singleSelector, multiSelector, dropDown, dateSelector, timeSelector, phoneNumber, uniqueNumbering, file, gpsLocation, html, calculationsAndLogic, codeScanner, counter, slider, signature, validation, liveTracking, nfcReader, address",
    )
    label: str = Field(min_length=1, description="Label for the field")
    options: Optional[List[str]] = Field(None, description="Options for selector/dropdown fields")
    
    @field_validator('options')
    def validate_options(cls, v: List[str], values: ValidationInfo) -> List[str]:
        field_type = values.data.get('field_type')
        if field_type in ["singleSelector", "multiSelector", "dropDown"]:
            if not v:
                raise ValueError(f"Options are required for {field_type}")
            if not isinstance(v, list) or not all(isinstance(opt, str) for opt in v):
                raise ValueError("Options must be a list of strings")
        return v
    
    def to_dict(self) -> Dict[str, Any]:
        result = {
            "fieldType": self.field_type.value,
            "label": self.label,
        }
        if self.options is not None:
            result["options"] = self.options
        return result

class AppSection(BaseModel):
    section_name: str = Field(min_length=1, description="Name of the section")
    fields: List[AppField] = Field(min_length=1, description="Array of fields in this section")
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "sectionName": self.section_name,
            "fields": [field.to_dict() for field in self.fields]
        }