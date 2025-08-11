from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field
from .base_response import BaseResponse
from ...enums import ChartType

class ChartResponse(BaseResponse):
    app_id: str = Field(None, description="App ID")
    chart_index: Optional[int] = Field(None, description="Index of the chart")
    chart_type: Optional[ChartType] = Field(None, description="Type of chart")
    operation: str = Field(description="Type of operation performed")

class ChartDefinition(BaseModel):
    chart_id: str = Field(description="Unique identifier for the chart")
    chart_type: ChartType = Field(description="Type of chart")
    chart_title: Optional[str] = Field(None, description="Title of the chart")
    configuration: Optional[Dict[str, Any]] = Field(None, description="Chart configuration")
