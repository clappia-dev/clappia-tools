from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, EmailStr, field_validator, ValidationInfo, model_validator
import re
from ...enums import ChartType


class BaseAnalyticsRequest(BaseModel):
    """Base class for analytics requests with common validation"""

    app_id: str = Field(description="App Id")

    class Config:
        extra = "forbid"


    @field_validator("app_id")
    @classmethod
    def validate_app_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()


class AddChartRequest(BaseAnalyticsRequest):
    """Request model for adding a chart to analytics dashboard"""

    chart_index: int = Field(ge=0, description="Chart position index (non-negative)")
    chart_type: ChartType = Field(description="Type of chart to add")
    chart_title: str = Field(default="", description="Chart title")
    
    class Config:
        extra = "allow"

    @field_validator("chart_index")
    @classmethod
    def validate_chart_index(cls, v: int) -> int:
        if v < 0:
            raise ValueError('Parameter "chartIndex" should be a non-negative number')
        return v

    @field_validator("chart_type")
    @classmethod
    def validate_chart_type(cls, v: ChartType) -> ChartType:
        if v not in ChartType:
            allowed_values = ", ".join([ct.value for ct in ChartType])
            raise ValueError(
                f'Parameter "chartType" is not valid, allowed values are: {allowed_values}'
            )
        return v

    @model_validator(mode='before')
    @classmethod
    def validate_required_fields(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        if isinstance(values, dict):
            if 'chart_index' in values and (not isinstance(values['chart_index'], int) or values['chart_index'] < 0):
                raise ValueError('Parameter "chartIndex" should be a non-negative number')
            if 'chart_type' not in values:
                raise ValueError('Parameter "chartType" is required')
        return values

    def get_extra_fields(self) -> Dict[str, Any]:
        """Get all extra fields that were passed beyond the defined schema"""
        base_fields = {
            'app_id', 'chart_index', 'chart_type', 'chart_title'
        }
        all_fields = set(self.model_dump().keys())
        extra_field_names = all_fields - base_fields
        return {field: getattr(self, field) for field in extra_field_names if hasattr(self, field)}

class UpdateChartRequest(BaseAnalyticsRequest):
    """Request model for updating a chart in analytics dashboard"""

    chart_index: int = Field(ge=0, description="Chart position index (non-negative)")
    chart_title: Optional[str] = Field(None, description="Updated chart title")
    
    class Config:
        extra = "allow"

    @field_validator("chart_index")
    @classmethod
    def validate_chart_index(cls, v: int) -> int:
        if v < 0:
            raise ValueError('Parameter "chartIndex" should be a non-negative number')
        return v

    @model_validator(mode='before')
    @classmethod
    def validate_required_fields(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        if isinstance(values, dict):
            if 'chart_index' in values and (not isinstance(values['chart_index'], int) or values['chart_index'] < 0):
                raise ValueError('Parameter "chartIndex" should be a non-negative number')
        return values

    def get_extra_fields(self) -> Dict[str, Any]:
        """Get all extra fields that were passed beyond the defined schema"""
        base_fields = {
            'app_id', 'chart_index', 'chart_title'
        }
        all_fields = set(self.model_dump().keys())
        extra_field_names = all_fields - base_fields
        return {field: getattr(self, field) for field in extra_field_names if hasattr(self, field)}


class ReorderChartRequest(BaseAnalyticsRequest):
    """Request model for reordering charts"""

    source_index: int = Field(description="Current index of the chart to move")
    target_index: int = Field(description="New index where to move the chart")

    @field_validator("source_index")
    @classmethod
    def validate_source_index(cls, v: int) -> int:
        if not isinstance(v, int) or v < 0:
            raise ValueError('Parameter "sourceIndex" should be a non-negative number')
        return v

    @field_validator("target_index")
    @classmethod
    def validate_target_index(cls, v: int) -> int:
        if not isinstance(v, int) or v < 0:
            raise ValueError(
                'Parameter "targetChartIndex" should be a non-negative number'
            )
        return v

    @field_validator("target_index")
    @classmethod
    def validate_different_indices(cls, v: int, info: ValidationInfo) -> int:
        if "source_index" in info.data and v == info.data["source_index"]:
            raise ValueError("Source and target chart indices cannot be the same")
        return v

class GetAppChartsRequest(BaseAnalyticsRequest):
    """Request model for getting charts definition"""
    pass