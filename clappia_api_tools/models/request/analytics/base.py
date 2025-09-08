from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict, field_validator
import re
import json
from urllib.parse import urlparse
from enum import Enum
from datetime import datetime, date
from .model import ExternalFilter


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
        components = snake_str.split("_")
        return components[0] + "".join(word.capitalize() for word in components[1:])


class BaseFieldComponent(BaseModel, JsonSerializableMixin):
    """Base component for field-related models"""

    model_config = ConfigDict(str_strip_whitespace=True, validate_assignment=True)


class ValidatedString(str):
    """Custom string type with common validation patterns"""

    @classmethod
    def non_empty_string_validator(
        cls, v: Optional[str], field_name: str = "Field"
    ) -> Optional[str]:
        if v is not None and (not v or not v.strip()):
            raise ValueError(f"{field_name} cannot be empty")
        return v.strip() if v else v

    @classmethod
    def number_validator(
        cls, v: Optional[int], field_name: str = "Field"
    ) -> Optional[int]:
        if v is not None and (not v or not v.strip()):
            raise ValueError(f"{field_name} cannot be empty")
        return v.strip() if v else v


class BaseUpsertChartRequest(BaseModel, JsonSerializableMixin):
    model_config = ConfigDict(str_strip_whitespace=True, validate_assignment=True)
    chart_title: str = Field(default="", description="Title of the chart")
    width: int = Field(default=50, description="Width of the chart")
    filters: Optional[List[ExternalFilter]] = Field(
        default=None, description="Filters for the chart"
    )
