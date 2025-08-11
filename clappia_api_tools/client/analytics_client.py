from typing import Dict, Any, Optional
from .base_client import BaseClappiaClient
from clappia_api_tools.utils.logging_utils import get_logger
from clappia_api_tools.models.request import (
    AddChartRequest, RemoveChartRequest, UpdateChartRequest, ReorderChartRequest
)
from clappia_api_tools.models.response import ChartResponse

logger = get_logger(__name__)

class AnalyticsClient(BaseClappiaClient):
    """Client for managing Clappia analytics and charts.
    
    This client handles retrieving and managing analytics configurations, including
    adding charts, removing charts, updating charts, and reordering charts.
    """
    
    def add_chart(self, app_id: str, chart_type: str, requesting_user_email_address: str,
                  chart_index: int = 0, chart_title: Optional[str] = None) -> ChartResponse:
        try:
            request = AddChartRequest(
                app_id=app_id,
                workplace_id=self.workplace_id,
                requesting_user_email_address=requesting_user_email_address,
                chart_type=chart_type,
                chart_index=chart_index,
                chart_title=chart_title
            )
        except Exception as e:
            return ChartResponse(
                success=False,
                message=str(e),
                app_id=app_id,
                operation="add"
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                operation="add"
            )

        payload = {
            "appId": request.app_id,
            "workplaceId": request.workplace_id,
            "chartType": request.chart_type.value,
            "chartIndex": request.chart_index,
            "requestingUserEmailAddress": str(request.requesting_user_email_address)
        }

        if request.chart_title:
            payload["chartTitle"] = request.chart_title

        logger.info(f"Adding chart for app_id: {app_id} with chart_type: {chart_type}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="analytics/addChart",
            data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                operation="add"
            )

        return ChartResponse(
            success=True,
            message="Successfully added chart",
            app_id=app_id,
            chart_type=chart_type,
            operation="add",
            data=response_data
        )

    def remove_chart(self, app_id: str, chart_index: int, 
                    requesting_user_email_address: str) -> ChartResponse:
        try:
            request = RemoveChartRequest(
                app_id=app_id,
                workplace_id=self.workplace_id,
                requesting_user_email_address=requesting_user_email_address,
                chart_index=chart_index
            )
        except Exception as e:
            return ChartResponse(
                success=False,
                message=str(e),
                app_id=app_id,
                operation="remove"
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                operation="remove"
            )

        payload = {
            "appId": request.app_id,
            "workplaceId": request.workplace_id,
            "chartIndex": request.chart_index,
            "requestingUserEmailAddress": str(request.requesting_user_email_address)
        }

        logger.info(f"Removing chart for app_id: {app_id} at index: {chart_index}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="analytics/removeChart",
            data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                operation="remove"
            )

        return ChartResponse(
            success=True,
            message="Successfully removed chart",
            app_id=app_id,
            chart_index=chart_index,
            operation="remove",
            data=response_data
        )

    def update_chart(self, app_id: str, chart_index: int, requesting_user_email_address: str,
                    update_data: Dict[str, Any]) -> ChartResponse:
        try:
            request = UpdateChartRequest(
                app_id=app_id,
                workplace_id=self.workplace_id,
                requesting_user_email_address=requesting_user_email_address,
                chart_index=chart_index,
                **update_data
            )
        except Exception as e:
            return ChartResponse(
                success=False,
                message=str(e),
                app_id=app_id,
                operation="update"
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                operation="update"
            )

        payload = {
            "appId": request.app_id,
            "workplaceId": request.workplace_id,
            "chartIndex": request.chart_index,
            "requestingUserEmailAddress": str(request.requesting_user_email_address),
            **update_data
        }

        logger.info(f"Updating chart for app_id: {app_id} at index: {chart_index}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="analytics/updateChart",
            data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                operation="update"
            )

        return ChartResponse(
            success=True,
            message="Successfully updated chart",
            app_id=app_id,
            chart_index=chart_index,
            operation="update",
            data=response_data
        )

    def reorder_chart(self, app_id: str, source_chart_index: int, target_chart_index: int,
                     requesting_user_email_address: str) -> ChartResponse:
        try:
            request = ReorderChartRequest(
                app_id=app_id,
                workplace_id=self.workplace_id,
                requesting_user_email_address=requesting_user_email_address,
                source_index=source_chart_index,
                target_index=target_chart_index
            )
        except Exception as e:
            return ChartResponse(
                success=False,
                message=str(e),
                app_id=app_id,
                operation="reorder"
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                operation="reorder"
            )

        payload = {
            "appId": request.app_id,
            "workplaceId": request.workplace_id,
            "sourceIndex": request.source_index,
            "targetIndex": request.target_index,
            "requestingUserEmailAddress": str(request.requesting_user_email_address)
        }

        logger.info(f"Reordering chart for app_id: {app_id} from index {source_chart_index} to {target_chart_index}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="analytics/reorderChart",
            data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                operation="reorder"
            )

        return ChartResponse(
            success=True,
            message="Successfully reordered chart",
            app_id=app_id,
            chart_index=source_chart_index,
            operation="reorder",
            data=response_data
        ) 