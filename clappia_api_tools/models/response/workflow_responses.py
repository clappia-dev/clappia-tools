from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field
from .base_response import BaseResponse
from ...enums import TriggerType
class WorkflowStep(BaseModel):
    node_id: str = Field(description="Unique identifier for the workflow step")
    node_type: str = Field(description="Type of workflow step")
    variable_name: str = Field(description="Variable name for the step")
    parameters: Optional[Dict[str, Any]] = Field(None, description="Step parameters")
    next_steps: Optional[List[str]] = Field(None, description="List of next step IDs")

class WorkflowTriggerDefinition(BaseModel):
    trigger_type: TriggerType = Field(description="Type of trigger")
    app_id: str = Field(description="App ID associated with the workflow")

class WorkflowLastUpdatedBy(BaseModel):
    name: str = Field(description="Name of the user who last updated the workflow")
    email_address: str = Field(description="Email address of the user who last updated the workflow")

class WorkflowResponse(BaseResponse):
    app_id: str = Field(None, description="App ID")
    trigger_definition: Optional[WorkflowTriggerDefinition] = Field(None, description="Workflow trigger definition")
    steps: Optional[List[WorkflowStep]] = Field(None, description="List of workflow steps")
    last_updated_by: Optional[WorkflowLastUpdatedBy] = Field(None, description="User who last updated the workflow")
    last_updated_at: Optional[str] = Field(None, description="Timestamp of last update")

class WorkflowStepResponse(BaseResponse):
    app_id: str = Field(None, description="App ID")
    trigger_type: TriggerType = Field(None, description="Trigger type")
    step_variable_name: Optional[str] = Field(None, description="Variable name of the affected step")
    operation: str = Field(description="Type of operation performed")
    parent_variable_name: Optional[str] = Field(None, description="Parent step variable name") 