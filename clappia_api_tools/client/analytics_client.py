from typing import Dict, Any, Optional
from .base_client import BaseClappiaClient
from clappia_api_tools.utils.logging_utils import get_logger
from clappia_api_tools.models.request import (
    AddChartRequest,
    RemoveChartRequest,
    UpdateChartRequest,
    ReorderChartRequest,
    GetAppChartsRequest
)
from clappia_api_tools.models.response import ChartResponse, GetAppChartsResponse, ChartDefinition

logger = get_logger(__name__)


class AnalyticsClient(BaseClappiaClient):
    """Client for managing Clappia analytics and charts.

    This client handles retrieving and managing analytics configurations, including
    adding charts, removing charts, updating charts, and reordering charts.
    """

    def add_chart(
        self,
        app_id: str,
        chart_type: str,
        chart_index: int = 0,
        chart_title: Optional[str] = None,
    ) -> ChartResponse:
        try:
            request = AddChartRequest(
                app_id=app_id,
                chart_type=chart_type,
                chart_index=chart_index,
                chart_title=chart_title,
            )
        except Exception as e:
            return ChartResponse(
                success=False, message=str(e), app_id=app_id, operation="add"
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False, message=env_error, app_id=app_id, operation="add"
            )

        payload = {
            "appId": request.app_id,
            "chartType": request.chart_type.value,
            "chartIndex": request.chart_index,
        }

        if request.chart_title:
            payload["chartTitle"] = request.chart_title

        logger.info(f"Adding chart for app_id: {app_id} with chart_type: {chart_type}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST", endpoint="analytics/addChart", data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False, message=error_message, app_id=app_id, operation="add"
            )

        return ChartResponse(
            success=True,
            message="Successfully added chart",
            app_id=app_id,
            chart_type=chart_type,
            operation="add",
            data=response_data,
        )

    def remove_chart(self, app_id: str, chart_index: int) -> ChartResponse:
        try:
            request = RemoveChartRequest(
                app_id=app_id,
                chart_index=chart_index,
            )
        except Exception as e:
            return ChartResponse(
                success=False, message=str(e), app_id=app_id, operation="remove"
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False, message=env_error, app_id=app_id, operation="remove"
            )

        payload = {
            "appId": request.app_id,
            "chartIndex": request.chart_index,
        }

        logger.info(f"Removing chart for app_id: {app_id} at index: {chart_index}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST", endpoint="analytics/removeChart", data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False, message=error_message, app_id=app_id, operation="remove"
            )

        return ChartResponse(
            success=True,
            message="Successfully removed chart",
            app_id=app_id,
            chart_index=chart_index,
            operation="remove",
            data=response_data,
        )

    def update_chart(
        self,
        app_id: str,
        chart_index: int,
        update_data: Dict[str, Any],
    ) -> ChartResponse:
        try:
            request = UpdateChartRequest(
                app_id=app_id,
                chart_index=chart_index,
                **update_data,
            )
        except Exception as e:
            return ChartResponse(
                success=False, message=str(e), app_id=app_id, operation="update"
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False, message=env_error, app_id=app_id, operation="update"
            )

        payload = {
            "appId": request.app_id,
            "chartIndex": request.chart_index,
            **update_data,
        }

        logger.info(f"Updating chart for app_id: {app_id} at index: {chart_index}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST", endpoint="analytics/updateChart", data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False, message=error_message, app_id=app_id, operation="update"
            )

        return ChartResponse(
            success=True,
            message="Successfully updated chart",
            app_id=app_id,
            chart_index=chart_index,
            operation="update",
            data=response_data,
        )

    def reorder_chart(
        self,
        app_id: str,
        source_index: int,
        target_index: int,
    ) -> ChartResponse:
        try:
            request = ReorderChartRequest(
                app_id=app_id,
                source_index=source_index,
                target_index=target_index,
            )
        except Exception as e:
            return ChartResponse(
                success=False, message=str(e), app_id=app_id, operation="reorder"
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return ChartResponse(
                success=False, message=env_error, app_id=app_id, operation="reorder"
            )

        payload = {
            "appId": request.app_id,
            "sourceIndex": request.source_index,
            "targetIndex": request.target_index,
        }

        logger.info(
            f"Reordering chart for app_id: {app_id} from index {source_index} to {target_index}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST", endpoint="analytics/reorderChart", data=payload
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return ChartResponse(
                success=False, message=error_message, app_id=app_id, operation="reorder"
            )

        return ChartResponse(
            success=True,
            message="Successfully reordered chart",
            app_id=app_id,
            chart_index=source_index,
            operation="reorder",
            data=response_data,
        )
    
    def get_charts(self, app_id: str) -> GetAppChartsResponse:
        """Get all charts for a specific app.

        Args:
            app_id: The ID of the app to get charts for

        Returns:
            GetAppChartsResponse: Response containing the list of charts
        """
        try:
            request = GetAppChartsRequest(app_id=app_id)
        except Exception as e:
            return GetAppChartsResponse(
                success=False, message=str(e), app_id=app_id, operation="get"
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return GetAppChartsResponse(
                success=False, message=env_error, app_id=app_id, operation="get"
            )
        params = {
            "appId": request.app_id,
        }

        logger.info(f"Getting charts for app_id: {app_id}")

        success, error_message, response_data = self.api_utils.make_request(
            method="GET", endpoint="analytics/getAppCharts", params=params
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return GetAppChartsResponse(
                success=False, message=error_message, app_id=app_id, operation="get"
            )
        return GetAppChartsResponse(
            success=True,
            message="Successfully retrieved charts",
            app_id=app_id,
            operation="get_charts",
            data=response_data,
        )
