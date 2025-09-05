from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict, field_validator
import re
import json
from urllib.parse import urlparse
from enum import Enum
from datetime import datetime, date

class JsonSerializableMixin:
    """Mixin to provide robust JSON serialization functionality."""

    def to_json(self) -> Dict[str, Any]:
        """Convert the object to a JSON-serializable dictionary."""
        def _serialize(value: Any) -> Any:
            if hasattr(value, "to_json"):
                return value.to_json()
            elif isinstance(value, dict):
                return {k: _serialize(v) for k, v in value.items()}
            elif isinstance(value, list):
                return [_serialize(v) for v in value]
            elif isinstance(value, tuple) or isinstance(value, set):
                return [_serialize(v) for v in value]
            elif isinstance(value, Enum):
                return value.value
            elif isinstance(value, (datetime, date)):
                return value.isoformat()
            else:
                return value

        data = {}
        for field_name, field_value in self.__dict__.items():
            if field_value is not None:
                camel_case_key = self._to_camel_case(field_name)
                data[camel_case_key] = _serialize(field_value)

        return data

    @staticmethod
    def _to_camel_case(snake_str: str) -> str:
        components = snake_str.split('_')
        return components[0] + ''.join(word.capitalize() for word in components[1:])


class ValidatedString(str):
    """Custom string type with common validation patterns"""
    
    @classmethod
    def non_empty_string_validator(cls, v: Optional[str], field_name: str = "Field") -> Optional[str]:
        if v is not None and (not v or not v.strip()):
            raise ValueError(f"{field_name} cannot be empty")
        return v.strip() if v else v
    
    @classmethod
    def number_validator(cls, v: Optional[int], field_name: str = "Field") -> Optional[int]:
        if v is not None and (not v or not v.strip()):
            raise ValueError(f"{field_name} cannot be empty")
        return v.strip() if v else v

class BaseUpsertWorkflowStepRequest(BaseModel, JsonSerializableMixin):
    model_config = ConfigDict(str_strip_whitespace=True, validate_assignment=True)
    name: str = Field(description="Name of the workflow step")
    field_name: Optional[str] = Field(None, description="Field name of the workflow step")
    enabled: bool = Field(default=True, description="Whether the workflow step is enabled")
    public_urls_expiry: int = Field(default=-1, description="Public URLs expiry")

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        return ValidatedString.non_empty_string_validator(v, "Name")