from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, EmailStr, field_validator, ValidationInfo
import re
from ...enums import ChartType


class BaseAnalyticsRequest(BaseModel):
    """Base class for analytics requests with common validation"""

    app_id: str = Field(description="App Id")

    @field_validator("app_id")
    @classmethod
    def validate_app_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()


class AddChartRequest(BaseAnalyticsRequest):
    """Request model for adding a chart"""

    chart_index: int = Field(description="Index where to add the chart")
    chart_type: ChartType = Field(description="Type of chart to add")
    chart_title: Optional[str] = Field(None, description="Title for the chart")

    @field_validator("chart_index")
    @classmethod
    def validate_chart_index(cls, v: int) -> int:
        if not isinstance(v, int) or v < 0:
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

    @field_validator("chart_title")
    @classmethod
    def validate_chart_title(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            return v.strip() if v.strip() else ""
        return ""


class RemoveChartRequest(BaseAnalyticsRequest):
    """Request model for removing a chart"""

    chart_index: int = Field(description="Index of the chart to remove")

    @field_validator("chart_index")
    @classmethod
    def validate_chart_index(cls, v: int) -> int:
        if not isinstance(v, int) or v < 0:
            raise ValueError('Parameter "chartIndex" should be a non-negative number')
        return v


class UpdateChartRequest(BaseAnalyticsRequest):
    """Request model for updating a chart"""

    chart_index: int = Field(description="Index of the chart to update")

    @field_validator("chart_index")
    @classmethod
    def validate_chart_index(cls, v: int) -> int:
        if not isinstance(v, int) or v < 0:
            raise ValueError('Parameter "chartIndex" should be a non-negative number')
        return v


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