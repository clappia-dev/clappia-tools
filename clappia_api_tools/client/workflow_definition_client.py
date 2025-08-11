from typing import Dict, Any, Optional
from .base_client import BaseClappiaClient
from clappia_api_tools.utils.logging_utils import get_logger
from clappia_api_tools.models.request import (
    GetWorkflowRequest, AddWorkflowStepRequest, RemoveWorkflowStepRequest,
    UpdateWorkflowStepRequest, ReorderWorkflowStepRequest
)
from clappia_api_tools.models.response import WorkflowResponse, WorkflowStepResponse

logger = get_logger(__name__)

class WorkflowDefinitionClient(BaseClappiaClient):
    """Client for managing Clappia workflow definitions.
    
    This client handles retrieving and managing workflow definitions, including
    getting workflows, adding workflow steps, removing workflow steps,
    updating workflow steps, and reordering workflow steps.
    """
    
    def get_workflow(self, app_id: str, trigger_type: str, 
                     requesting_user_email_address: str) -> WorkflowResponse:
        try:
            request = GetWorkflowRequest(
                app_id=app_id,
                requesting_user_email_address=requesting_user_email_address,
                trigger_type=trigger_type
            )
        except Exception as e:
            return WorkflowResponse(
                success=False,
                message=str(e),
                app_id=app_id
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowResponse(
                success=False,
                message=env_error,
                app_id=app_id
            )

        params = {
            "appId": request.app_id,
            "triggerType": request.trigger_type.value,
            "requestingUserEmailAddress": str(request.requesting_user_email_address)
        }

        logger.info(f"Getting workflow for app_id: {app_id} with trigger_type: {trigger_type}")

        success, error_message, response_data = self.api_utils.make_request(
            method="GET",
            endpoint="workflowdefinitionv2/getWorkflow",
            params=params
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowResponse(
                success=False,
                message=error_message,
                app_id=app_id
            )

        return WorkflowResponse(
            success=True,
            message="Successfully retrieved workflow definition",
            app_id=app_id,
            data=response_data
        )

    def add_workflow_step(self, app_id: str, trigger_type: str, node_type: str,
                         requesting_user_email_address: str, 
                         parent_variable_name: str = "Start") -> WorkflowStepResponse:
        try:
            request = AddWorkflowStepRequest(
                app_id=app_id,
                requesting_user_email_address=requesting_user_email_address,
                trigger_type=trigger_type,
                node_type=node_type,
                parent_variable_name=parent_variable_name
            )
        except Exception as e:
            return WorkflowStepResponse(
                success=False,
                message=str(e),
                app_id=app_id,
                trigger_type=trigger_type,
                operation="add"
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                trigger_type=trigger_type,
                operation="add"
            )

        payload = {
            "appId": request.app_id,
            "triggerType": request.trigger_type.value,
            "nodeType": request.node_type,
            "parentVariableName": request.parent_variable_name,
            "requestingUserEmailAddress": str(request.requesting_user_email_address)
        }

        logger.info(f"Adding workflow step for app_id: {app_id} with node_type: {node_type}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/addWorkflowStep",
            data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                trigger_type=trigger_type,
                operation="add"
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully added workflow step",
            app_id=app_id,
            trigger_type=trigger_type,
            operation="add",
            data=response_data
        )

    def remove_workflow_step(self, app_id: str, trigger_type: str, step_variable_name: str,
                           requesting_user_email_address: str) -> WorkflowStepResponse:
        try:
            request = RemoveWorkflowStepRequest(
                app_id=app_id,
                requesting_user_email_address=requesting_user_email_address,
                trigger_type=trigger_type,
                step_variable_name=step_variable_name
            )
        except Exception as e:
            return WorkflowStepResponse(
                success=False,
                message=str(e),
                app_id=app_id,
                trigger_type=trigger_type,
                operation="remove"
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                trigger_type=trigger_type,
                operation="remove"
            )

        payload = {
            "appId": request.app_id,
            "triggerType": request.trigger_type.value,
            "stepVariableName": request.step_variable_name,
            "requestingUserEmailAddress": str(request.requesting_user_email_address)
        }

        logger.info(f"Removing workflow step for app_id: {app_id} with step: {step_variable_name}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/removeWorkflowStep",
            data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                trigger_type=trigger_type,
                operation="remove"
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully removed workflow step",
            app_id=app_id,
            trigger_type=trigger_type,
            operation="remove",
            step_variable_name=step_variable_name,
            data=response_data
        )

    def update_workflow_step(self, app_id: str, trigger_type: str, step_variable_name: str,
                           requesting_user_email_address: str, 
                           update_data: Dict[str, Any]) -> WorkflowStepResponse:
        try:
            request = UpdateWorkflowStepRequest(
                app_id=app_id,
                requesting_user_email_address=requesting_user_email_address,
                trigger_type=trigger_type,
                step_variable_name=step_variable_name,
                **update_data
            )
        except Exception as e:
            return WorkflowStepResponse(
                success=False,
                message=str(e),
                app_id=app_id,
                trigger_type=trigger_type,
                operation="update"
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                trigger_type=trigger_type,
                operation="update"
            )

        payload = {
            "appId": request.app_id,
            "triggerType": request.trigger_type.value,
            "stepVariableName": request.step_variable_name,
            "requestingUserEmailAddress": str(request.requesting_user_email_address),
            **update_data
        }

        logger.info(f"Updating workflow step for app_id: {app_id} with step: {step_variable_name}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/updateWorkflowStep",
            data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                trigger_type=trigger_type,
                operation="update"
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully updated workflow step",
            app_id=app_id,
            trigger_type=trigger_type,
            operation="update",
            step_variable_name=step_variable_name,
            data=response_data
        )

    def reorder_workflow_step(self, app_id: str, trigger_type: str, step_variable_name: str,
                             parent_variable_name: str, requesting_user_email_address: str) -> WorkflowStepResponse:
        try:
            request = ReorderWorkflowStepRequest(
                app_id=app_id,
                requesting_user_email_address=requesting_user_email_address,
                trigger_type=trigger_type,
                step_variable_name=step_variable_name,
                parent_variable_name=parent_variable_name
            )
        except Exception as e:
            return WorkflowStepResponse(
                success=False,
                message=str(e),
                app_id=app_id,
                trigger_type=trigger_type,
                operation="reorder"
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return WorkflowStepResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                trigger_type=trigger_type,
                operation="reorder"
            )

        payload = {
            "appId": request.app_id,
            "triggerType": request.trigger_type.value,
            "stepVariableName": request.step_variable_name,
            "parentVariableName": request.parent_variable_name,
            "requestingUserEmailAddress": str(request.requesting_user_email_address)
        }

        logger.info(f"Reordering workflow step for app_id: {app_id} with step: {step_variable_name}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="workflowdefinitionv2/reorderWorkflowStep",
            data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return WorkflowStepResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                trigger_type=trigger_type,
                operation="reorder"
            )

        return WorkflowStepResponse(
            success=True,
            message="Successfully reordered workflow step",
            app_id=app_id,
            trigger_type=trigger_type,
            operation="reorder",
            step_variable_name=step_variable_name,
            parent_variable_name=parent_variable_name,
            data=response_data
        )
