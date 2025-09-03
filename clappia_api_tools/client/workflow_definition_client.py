from typing import Dict, Any, Optional
from .base_client import BaseClappiaClient
from clappia_api_tools.utils.logging_utils import get_logger
from clappia_api_tools.models.request import (
    GetWorkflowRequest,
    AddWorkflowStepRequest,
    UpdateWorkflowStepRequest,
    ReorderWorkflowStepRequest,
)
from clappia_api_tools.models.response import WorkflowResponse, WorkflowStepResponse, BaseResponse

logger = get_logger(__name__)


class WorkflowDefinitionClient(BaseClappiaClient):
    """Client for managing Clappia workflow definitions.

    This client handles retrieving and managing workflow definitions, including
    getting workflows, adding workflow steps, removing workflow steps,
    updating workflow steps, and reordering workflow steps.
    """

    def get_workflow(self, app_id: str, trigger_type: str) -> WorkflowResponse:
        try:
            request = GetWorkflowRequest(
                app_id=app_id,
                trigger_type=trigger_type,
            )
        except Exception as e:
            return WorkflowResponse(success=False, message=str(e), app_id=app_id, operation="get_workflow")

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowResponse(success=False, message=env_error, app_id=app_id, operation="get_workflow")

        params = {
            "appId": request.app_id,
            "triggerType": request.trigger_type.value,
        }

        logger.info(
            f"Getting workflow for app_id: {app_id} with trigger_type: {trigger_type}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="GET", endpoint="workflowdefinitionv2/getWorkflow", params=params
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowResponse(success=False, message=error_message, app_id=app_id, operation="get_workflow")

        return WorkflowResponse(
            success=True,
            message="Successfully retrieved workflow definition",
            app_id=app_id,
            data=response_data,
            operation="get_workflow",
        )

    def add_workflow_step(
        self,
        app_id: str,
        trigger_type: str,
        node_type: str,
        parent_variable_name: Optional[str] = None,
        **kwargs
    ) -> WorkflowStepResponse:
        """Add a workflow step to a Clappia app"""
        try:
            request = AddWorkflowStepRequest(
                app_id=app_id,
                trigger_type=trigger_type,
                node_type=node_type,
                parent_variable_name=parent_variable_name,
                **kwargs
            )
        except Exception as e:
            return WorkflowStepResponse(
                success=False,
                message=str(e),
                app_id=app_id,
                trigger_type=trigger_type,
                operation="add",
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                trigger_type=trigger_type,
                operation="add",
            )

        payload = {
            "appId": request.app_id,
            "triggerType": request.trigger_type.value if hasattr(request.trigger_type, 'value') else request.trigger_type,
            "nodeType": request.node_type.value,
            "parentVariableName": request.parent_variable_name,
        }
        
        extra_fields = request.get_extra_fields()
        payload.update(extra_fields)

        logger.info(
            f"Adding workflow step for app_id: {app_id} with node_type: {node_type}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST", endpoint="workflowdefinitionv2/addWorkflowStep", data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                trigger_type=trigger_type,
                operation="add",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully added workflow step",
            app_id=app_id,
            trigger_type=trigger_type,
            operation="add",
            data=response_data,
        )

    def update_workflow_step(
        self,
        app_id: str,
        trigger_type: str,
        step_variable_name: str,
        update_data: Dict[str, Any],
    ) -> WorkflowStepResponse:
        """Update a workflow step in a Clappia app"""
        try:
            request = UpdateWorkflowStepRequest(
                app_id=app_id,
                trigger_type=trigger_type,
                step_variable_name=step_variable_name,
                **update_data,
            )
        except Exception as e:
            return WorkflowStepResponse(
                success=False,
                message=str(e),
                app_id=app_id,
                trigger_type=trigger_type,
                operation="update",
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                trigger_type=trigger_type,
                operation="update",
            )

        payload = {
            "appId": request.app_id,
            "triggerType": request.trigger_type.value if hasattr(request.trigger_type, 'value') else request.trigger_type,
            "stepVariableName": request.step_variable_name,
            **update_data,
        }

        logger.info(
            f"Updating workflow step for app_id: {app_id} with step: {step_variable_name}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/updateWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                trigger_type=trigger_type,
                operation="update",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully updated workflow step",
            app_id=app_id,
            trigger_type=trigger_type,
            operation="update",
            step_variable_name=step_variable_name,
            data=response_data,
        )

    def reorder_workflow_step(
        self,
        app_id: str,
        trigger_type: str,
        step_variable_name: str,
        parent_variable_name: str,
    ) -> WorkflowStepResponse:
        try:
            request = ReorderWorkflowStepRequest(
                app_id=app_id,
                trigger_type=trigger_type,
                step_variable_name=step_variable_name,
                parent_variable_name=parent_variable_name,
            )
        except Exception as e:
            return WorkflowStepResponse(
                success=False,
                message=str(e),
                app_id=app_id,
                trigger_type=trigger_type,
                operation="reorder",
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                trigger_type=trigger_type,
                operation="reorder",
            )

        payload = {
            "appId": request.app_id,
            "triggerType": request.trigger_type.value,
            "stepVariableName": request.step_variable_name,
            "parentVariableName": request.parent_variable_name,
        }

        logger.info(
            f"Reordering workflow step for app_id: {app_id} with step: {step_variable_name}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/reorderWorkflowStep",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                trigger_type=trigger_type,
                operation="reorder",
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully reordered workflow step",
            app_id=app_id,
            trigger_type=trigger_type,
            operation="reorder",
            step_variable_name=step_variable_name,
            parent_variable_name=parent_variable_name,
            data=response_data,
        )

    def get_schema(self) -> BaseResponse:
        """Get the schema for workflow definitions.

        Returns:
            WorkflowResponse: Response containing the workflow schema
        """
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return BaseResponse(
                success=False, 
                message=env_error, 
                operation="get_schema"
            )

        logger.info("Getting workflow schema")

        success, error_message, response_data = self.api_utils.make_request(
            method="GET", 
            endpoint="workflowdefinitionv2/schema"
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return BaseResponse(
                success=False, 
                message=error_message, 
                operation="get_schema"
            )

        return BaseResponse(
            success=True,
            message="Successfully retrieved workflow schema",
            data=response_data,
            operation="get_schema",
        )
