from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, EmailStr, field_validator, ValidationInfo
import re
from ...enums import TriggerType, NodeType


class BaseWorkflowRequest(BaseModel):
    """Base class for workflow requests with common validation"""

    app_id: str = Field(description="App Id")
    trigger_type: TriggerType = Field(description="Trigger type for the workflow")

    @field_validator("app_id")
    @classmethod
    def validate_app_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("App ID is required and cannot be empty")
        if not re.match(r"^[A-Z0-9]+$", v.strip()):
            raise ValueError("App ID must contain only uppercase letters and numbers")
        return v.strip()

    @field_validator("trigger_type")
    @classmethod
    def validate_trigger_type(cls, v: TriggerType) -> TriggerType:
        if v not in TriggerType:
            allowed_values = ", ".join([tt.value for tt in TriggerType])
            raise ValueError(
                f"Parameter triggerType is not valid, valid values are {allowed_values}"
            )
        return v


class AddWorkflowStepRequest(BaseWorkflowRequest):
    """Request model for adding a workflow step"""

    parent_variable_name: Optional[str] = Field(
        None, description="Parent workflow step variable name"
    )
    node_type: NodeType = Field(description="Type of workflow node to add")

    @field_validator("node_type")
    @classmethod
    def validate_node_type(cls, v: NodeType) -> NodeType:
        if v not in NodeType:
            allowed_values = ", ".join([nt.value for nt in NodeType])
            raise ValueError(
                f"Parameter nodeType is not valid, valid values are {allowed_values}"
            )
        return v

    @field_validator("parent_variable_name")
    @classmethod
    def validate_parent_variable_name(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            return v.strip() if v.strip() else None
        return None


class RemoveWorkflowStepRequest(BaseWorkflowRequest):
    """Request model for removing a workflow step"""

    step_variable_name: str = Field(
        description="Variable name of the workflow step to remove"
    )
    delete_type: str = Field(description="Type of deletion: 'subtree' or 'node'")

    @field_validator("step_variable_name")
    @classmethod
    def validate_step_variable_name(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Parameter stepVariableName is required")
        return v.strip()

    @field_validator("delete_type")
    @classmethod
    def validate_delete_type(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Parameter deleteType is required")
        if v not in ["subtree", "node"]:
            raise ValueError(
                "Parameter deleteType is not valid, valid values are subtree, node"
            )
        return v.strip()


class UpdateWorkflowStepRequest(BaseWorkflowRequest):
    """Request model for updating a workflow step"""

    step_variable_name: str = Field(
        description="Variable name of the workflow step to update"
    )

    @field_validator("step_variable_name")
    @classmethod
    def validate_step_variable_name(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Parameter stepVariableName is required")
        return v.strip()


class ReorderWorkflowStepRequest(BaseWorkflowRequest):
    """Request model for reordering workflow steps"""

    step_variable_name: str = Field(
        description="Variable name of the workflow step to move"
    )
    parent_variable_name: Optional[str] = Field(
        None, description="Variable name of the new parent workflow step"
    )

    @field_validator("step_variable_name")
    @classmethod
    def validate_step_variable_name(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Parameter stepVariableName is required")
        return v.strip()

class GetWorkflowRequest(BaseWorkflowRequest):
    """Request model for getting workflow information"""

    pass
