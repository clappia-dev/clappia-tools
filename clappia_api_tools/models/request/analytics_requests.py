from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, EmailStr, field_validator, ValidationInfo
import re
from ...enums import ChartType

# Email validation regex pattern
EMAIL_REGEX = re.compile(r'^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$')

def is_any_email_valid(email_ids: list[str]) -> bool:
    """Check if any email in the list is valid"""
    return any(
        EMAIL_REGEX.match(email.strip()) 
        for email in email_ids 
        if email and email.strip()
    )

class BaseAnalyticsRequest(BaseModel):
    """Base class for analytics requests with common validation"""
    app_id: str = Field(description="The Clappia app ID")
    workplace_id: str = Field(description="The workplace ID")
    requesting_user_email_address: str = Field(description="Email of requesting user")
    
    @field_validator('app_id')
    @classmethod
    def validate_app_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError('Parameter "appId" is required')
        return v.strip()
    
    @field_validator('workplace_id')
    @classmethod
    def validate_workplace_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError('Parameter "workplaceId" is required')
        return v.strip()
    
    @field_validator('requesting_user_email_address')
    @classmethod
    def validate_email(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError('Parameter requestingUserEmailAddress is required')
        if not is_any_email_valid([v]):
            raise ValueError(f'Parameter requestingUserEmailAddress is not valid with value: {v}')
        return v.strip()

class AddChartRequest(BaseAnalyticsRequest):
    """Request model for adding a chart"""
    chart_index: int = Field(description="Index where to add the chart")
    chart_type: ChartType = Field(description="Type of chart to add")
    chart_title: Optional[str] = Field(None, description="Title for the chart")
    
    @field_validator('chart_index')
    @classmethod
    def validate_chart_index(cls, v: int) -> int:
        if not isinstance(v, int) or v < 0:
            raise ValueError('Parameter "chartIndex" should be a non-negative number')
        return v
    
    @field_validator('chart_type')
    @classmethod
    def validate_chart_type(cls, v: ChartType) -> ChartType:
        if v not in ChartType:
            allowed_values = ', '.join([ct.value for ct in ChartType])
            raise ValueError(f'Parameter "chartType" is not valid, allowed values are: {allowed_values}')
        return v
    
    @field_validator('chart_title')
    @classmethod
    def validate_chart_title(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            return v.strip() if v.strip() else ''
        return ''

class RemoveChartRequest(BaseAnalyticsRequest):
    """Request model for removing a chart"""
    chart_index: int = Field(description="Index of the chart to remove")
    
    @field_validator('chart_index')
    @classmethod
    def validate_chart_index(cls, v: int) -> int:
        if not isinstance(v, int) or v < 0:
            raise ValueError('Parameter "chartIndex" should be a non-negative number')
        return v

class UpdateChartRequest(BaseAnalyticsRequest):
    """Request model for updating a chart"""
    chart_index: int = Field(description="Index of the chart to update")
    
    @field_validator('chart_index')
    @classmethod
    def validate_chart_index(cls, v: int) -> int:
        if not isinstance(v, int) or v < 0:
            raise ValueError('Parameter "chartIndex" should be a non-negative number')
        return v

class ReorderChartRequest(BaseAnalyticsRequest):
    """Request model for reordering charts"""
    source_index: int = Field(description="Current index of the chart to move")
    target_index: int = Field(description="New index where to move the chart")
    
    @field_validator('source_index')
    @classmethod
    def validate_source_index(cls, v: int) -> int:
        if not isinstance(v, int) or v < 0:
            raise ValueError('Parameter "sourceIndex" should be a non-negative number')
        return v
    
    @field_validator('target_index')
    @classmethod
    def validate_target_index(cls, v: int) -> int:
        if not isinstance(v, int) or v < 0:
            raise ValueError('Parameter "targetChartIndex" should be a non-negative number')
        return v
    
    @field_validator('target_index')
    @classmethod
    def validate_different_indices(cls, v: int, info: ValidationInfo) -> int:
        if 'source_index' in info.data and v == info.data['source_index']:
            raise ValueError('Source and target chart indices cannot be the same')
        return v