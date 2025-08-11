from typing import Optional
from pydantic import BaseModel, Field, EmailStr, field_validator, ValidationInfo
import re
from ...enums import TriggerType

class GetWorkflowRequest(BaseModel):
    app_id: str = Field(description="The Clappia app ID")
    requesting_user_email_address: EmailStr = Field(description="Email of requesting user")
    trigger_type: TriggerType = Field(description="Trigger type for the workflow, possible values are submissionCreated, submissionEdited, submissionStatusEdited, schedule")
    
    @field_validator('app_id')
    def validate_app_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()

class AddWorkflowStepRequest(BaseModel):
    app_id: str = Field(description="The Clappia app ID")
    requesting_user_email_address: EmailStr = Field(description="Email of requesting user")
    trigger_type: TriggerType = Field(description="Trigger type for the workflow, possible values are submissionCreated, submissionEdited, submissionStatusEdited, schedule")
    parent_variable_name: str = Field(default="Start", description="Parent workflow step variable name")
    node_type: str = Field(description="Type of workflow node to add")
    
    @field_validator('app_id')
    def validate_app_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()
    
    @field_validator('node_type')
    def validate_node_type(cls, v: str) -> str:
        valid_node_types = [
            "Email", "Slack", "WhatsApp", "Mobile", "SMS", "Sync", "Pass",
            "CreateClappiaAppSubmission", "EditClappiaAppSubmission", 
            "FindClappiaAppSubmission", "DeleteClappiaAppSubmission"
        ]
        if v not in valid_node_types:
            raise ValueError(f"Node type must be one of: {', '.join(valid_node_types)}")
        return v

class RemoveWorkflowStepRequest(BaseModel):
    app_id: str = Field(description="The Clappia app ID")
    requesting_user_email_address: EmailStr = Field(description="Email of requesting user")
    trigger_type: TriggerType = Field(description="Trigger type for the workflow, possible values are submissionCreated, submissionEdited, submissionStatusEdited, schedule")
    step_variable_name: str = Field(description="Variable name of the workflow step to remove")
    
    @field_validator('app_id')
    def validate_app_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()
    
    @field_validator('step_variable_name')
    def validate_step_variable_name(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Step variable name is required and cannot be empty")
        return v.strip()

class UpdateWorkflowStepRequest(BaseModel):
    app_id: str = Field(description="The Clappia app ID")
    requesting_user_email_address: EmailStr = Field(description="Email of requesting user")
    trigger_type: TriggerType = Field(description="Trigger type for the workflow, possible values are submissionCreated, submissionEdited, submissionStatusEdited, schedule")
    step_variable_name: str = Field(description="Variable name of the workflow step to update")
    new_variable_name: Optional[str] = Field(None, description="New variable name for the step")
    # Additional fields can be added based on the specific node type being updated
    
    @field_validator('app_id')
    def validate_app_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()
    
    @field_validator('step_variable_name')
    def validate_step_variable_name(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Step variable name is required and cannot be empty")
        return v.strip()
    
    @field_validator('new_variable_name')
    def validate_new_variable_name(cls, v: str, values: ValidationInfo) -> str:
        if v and 'step_variable_name' in values.data and v == values.data['step_variable_name']:
            raise ValueError("New variable name must be different from current variable name")
        return v

class ReorderWorkflowStepRequest(BaseModel):
    app_id: str = Field(description="The Clappia app ID")
    requesting_user_email_address: EmailStr = Field(description="Email of requesting user")
    trigger_type: TriggerType = Field(description="Trigger type for the workflow, possible values are submissionCreated, submissionEdited, submissionStatusEdited, schedule")
    step_variable_name: str = Field(description="Variable name of the workflow step to move")
    parent_variable_name: str = Field(description="Variable name of the new parent workflow step")
    
    @field_validator('app_id')
    def validate_app_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()
    
    @field_validator('step_variable_name')
    def validate_step_variable_name(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Step variable name is required and cannot be empty")
        return v.strip()
    
    @field_validator('parent_variable_name')
    def validate_parent_variable_name(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Parent variable name is required and cannot be empty")
        return v.strip() 