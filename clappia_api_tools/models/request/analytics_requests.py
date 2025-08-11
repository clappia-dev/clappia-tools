from typing import Optional
from pydantic import BaseModel, Field, EmailStr, field_validator
import re
from ...enums import ChartType

class AddChartRequest(BaseModel):
    app_id: str = Field(description="The Clappia app ID")
    requesting_user_email_address: EmailStr = Field(description="Email of requesting user")
    chart_index: Optional[int] = Field(None, ge=0, description="Index where to add the chart")
    chart_type: ChartType = Field(description="Type of chart to add")
    chart_title: Optional[str] = Field(None, description="Title for the chart")
    
    @field_validator('app_id')
    def validate_app_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()
    
    @field_validator('chart_type')
    def validate_chart_type(cls, v: str) -> str:
        valid_chart_types = [
            "Summary", "Pie", "Doughnut", "Bar", "Line", "Map", "Geo", "Gantt"
        ]
        if v not in valid_chart_types:
            raise ValueError(f"Chart type must be one of: {', '.join(valid_chart_types)}")
        return v

class RemoveChartRequest(BaseModel):
    app_id: str = Field(description="The Clappia app ID")
    requesting_user_email_address: EmailStr = Field(description="Email of requesting user")
    chart_index: int = Field(ge=0, description="Index of the chart to remove")
    
    @field_validator('app_id')
    def validate_app_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()

class UpdateChartRequest(BaseModel):
    app_id: str = Field(description="The Clappia app ID")
    requesting_user_email_address: EmailStr = Field(description="Email of requesting user")
    chart_index: int = Field(ge=0, description="Index of the chart to update")
    chart_title: Optional[str] = Field(None, description="New title for the chart")
    # Additional fields can be added based on the specific chart type being updated
    
    @field_validator('app_id')
    def validate_app_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()

class ReorderChartRequest(BaseModel):
    app_id: str = Field(description="The Clappia app ID")
    requesting_user_email_address: EmailStr = Field(description="Email of requesting user")
    source_chart_index: int = Field(ge=0, description="Current index of the chart to move")
    target_chart_index: int = Field(ge=0, description="New index where to move the chart")
    
    @field_validator('app_id')
    def validate_app_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip() 