import json
from .base_client import BaseClappiaClient
from clappia_api_tools.utils.logging_utils import get_logger
from typing import List, Dict, Any, Optional
from clappia_api_tools.models.request import (
    GetAppDefinitionRequest,
    CreateAppRequest,
    AddFieldRequest,
    AddSectionRequest,
    UpdateSectionRequest,
    UpdateFieldRequest,
    AddPageBreakRequest,
    UpdatePageBreakRequest,
    ReorderSectionRequest,

    AddFieldTextRequest,
    AddFieldTextAreaRequest,
    AddFieldDependencyAppRequest,
    AddFieldRestApiRequest,
    AddFieldAddressRequest,
    AddFieldDatabaseRequest,
    AddFieldDateRequest,
    AddFieldAIRequest,
    AddFieldCodeRequest,
    AddFieldCodeReaderRequest,
    AddFieldEmailInputRequest,
    AddFieldEmojiRequest,
    AddFieldFileRequest,
    AddFieldGpsLocationRequest,
    AddFieldLiveTrackingRequest,
    AddFieldManualAddressRequest,
    AddFieldPhoneNumberRequest,
    AddFieldProgressBarRequest,
    AddFieldSignatureRequest,
    AddFieldRangeRequest,
    AddFieldCounterRequest,
    AddFieldSliderRequest,
    AddFieldTimeRequest,
    AddFieldToggleRequest,
    AddFieldValidationRequest,
    AddFieldVideoViewerRequest,
    AddFieldVoiceRequest,
    AddFieldFormulaRequest,
    AddFieldImageViewerRequest,
    AddFieldRichTextEditorRequest,
    AddFieldNfcReaderRequest,
    AddFieldNumberInputRequest,
    AddFieldPdfViewerRequest,
    AddFieldReadOnlyFileRequest,
    AddFieldReadOnlyTextRequest,
    AddFieldTagsRequest,
    AddFieldUniqueSequentialRequest,
    AddFieldDropdownRequest,
    AddFieldRadioRequest,
    AddFieldUrlInputRequest,
    AddFieldCheckboxRequest,
    AddFieldPaymentGatewayRequest,
    AddFieldRazorpayPaymentGatewayRequest,
    AddFieldEazypayPaymentGatewayRequest,
    AddFieldPaypalPaymentGatewayRequest,
    AddFieldStripePaymentGatewayRequest,
    AddFieldButtonRequest,
)
from clappia_api_tools.models.definition import AppField, AppSection
from clappia_api_tools.models.response import (
    AppDefinitionResponse,
    AppCreationResponse,
    FieldOperationResponse,
    PageBreakOperationResponse,
    SectionOperationResponse,
    AddSectionResponse,
    UpdateSectionResponse,
)

logger = get_logger(__name__)


class AppDefinitionClient(BaseClappiaClient):
    """Client for managing Clappia app definitions.

    This client handles retrieving and managing app definitions, including
    getting app definitions, creating apps, adding fields, and updating fields.
    """

    def add_field_text(
    self,
    request: AddFieldTextRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_text",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding text field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding text field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_text",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added text field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_text",
            data=response_data,
        )


    def add_field_text_area(
        self,
        request: AddFieldTextAreaRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_textarea",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding textarea field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding textarea field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_textarea",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added textarea field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_textarea",
            data=response_data,
        )


    def add_field_dependency_app(
        self,
        request: AddFieldDependencyAppRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_dependency_app",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding dependency app field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding dependency app field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_dependency_app",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added dependency app field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_dependency_app",
            data=response_data,
        )


    def add_field_rest_api(
        self,
        request: AddFieldRestApiRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_rest_api",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding REST API field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding REST API field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_rest_api",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added REST API field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_rest_api",
            data=response_data,
        )


    def add_field_address(
        self,
        request: AddFieldAddressRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_address",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding address field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding address field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_address",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added address field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_address",
            data=response_data,
        )

    def add_field_database(
        self,
        request: AddFieldDatabaseRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_database",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding database field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding database field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_database",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added database field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_database",
            data=response_data,
        )

    def add_field_date(
        self,
        request: AddFieldDateRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_date",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding date field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding date field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_date",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added date field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_date",
            data=response_data,
        )

    def add_field_ai(
        self,
        request: AddFieldAIRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_ai",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding AI field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding AI field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_ai",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added AI field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_ai",
            data=response_data,
        )

    def add_field_code(
        self,
        request: AddFieldCodeRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_code",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding code field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding code field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_code",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added code field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_code",
            data=response_data,
        )

    def add_field_code_reader(
        self,
        request: AddFieldCodeReaderRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_code_reader",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding code reader field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding code reader field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_code_reader",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added code reader field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_code_reader",
            data=response_data,
        )

    def add_field_email_input(
        self,
        request: AddFieldEmailInputRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_email_input",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding email input field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding email input field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_email_input",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added email input field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_email_input",
            data=response_data,
        )

    def add_field_emoji(
        self,
        request: AddFieldEmojiRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_emoji",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding emoji field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding emoji field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_emoji",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added emoji field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_emoji",
            data=response_data,
        )

    def add_field_file(
        self,
        request: AddFieldFileRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_file",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding file field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding file field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_file",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added file field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_file",
            data=response_data,
        )

    def add_field_gps_location(
        self,
        request: AddFieldGpsLocationRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_gps_location",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding GPS location field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding GPS location field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_gps_location",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added GPS location field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_gps_location",
            data=response_data,
        )

    def add_field_live_tracking(
        self,
        request: AddFieldLiveTrackingRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_live_tracking",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding live tracking field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding live tracking field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_live_tracking",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added live tracking field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_live_tracking",
            data=response_data,
        )

    def add_field_manual_address(
        self,
        request: AddFieldManualAddressRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_manual_address",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding manual address field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding manual address field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_manual_address",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added manual address field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_manual_address",
            data=response_data,
        )

    def add_field_phone_number(
        self,
        request: AddFieldPhoneNumberRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_phone_number",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding phone number field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding phone number field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_phone_number",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added phone number field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_phone_number",
            data=response_data,
        )

    def add_field_progress_bar(
        self,
        request: AddFieldProgressBarRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_progress_bar",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding progress bar field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding progress bar field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_progress_bar",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added progress bar field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_progress_bar",
            data=response_data,
        )

    def add_field_signature(
        self,
        request: AddFieldSignatureRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_signature",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding signature field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding signature field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_signature",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added signature field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_signature",
            data=response_data,
        )

    def add_field_range(
        self,
        request: AddFieldRangeRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_range",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding range field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding range field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_range",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added range field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_range",
            data=response_data,
        )

    def add_field_counter(
        self,
        request: AddFieldCounterRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_counter",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding counter field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding counter field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_counter",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added counter field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_counter",
            data=response_data,
        )

    def add_field_slider(
        self,
        request: AddFieldSliderRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_slider",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding slider field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding slider field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_slider",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added slider field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_slider",
            data=response_data,
        )

    def add_field_time(
        self,
        request: AddFieldTimeRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_time",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding time field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding time field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_time",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added time field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_time",
            data=response_data,
        )

    def add_field_toggle(
        self,
        request: AddFieldToggleRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_toggle",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding toggle field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding toggle field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_toggle",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added toggle field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_toggle",
            data=response_data,
        )

    def add_field_validation(
        self,
        request: AddFieldValidationRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_validation",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding validation field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding validation field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_validation",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added validation field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_validation",
            data=response_data,
        )

    def add_field_video_viewer(
        self,
        request: AddFieldVideoViewerRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_video_viewer",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding video viewer field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding video viewer field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_video_viewer",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added video viewer field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_video_viewer",
            data=response_data,
        )

    def add_field_voice(
        self,
        request: AddFieldVoiceRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_voice",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding voice field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding voice field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_voice",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added voice field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_voice",
            data=response_data,
        )

    def add_field_formula(
        self,
        request: AddFieldFormulaRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_formula",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding formula field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding formula field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_formula",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added formula field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_formula",
            data=response_data,
        )

    def add_field_image_viewer(
        self,
        request: AddFieldImageViewerRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_image_viewer",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding image viewer field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding image viewer field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_image_viewer",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added image viewer field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_image_viewer",
            data=response_data,
        )

    def add_field_rich_text_editor(
        self,
        request: AddFieldRichTextEditorRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_rich_text_editor",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding rich text editor field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding rich text editor field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_rich_text_editor",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added rich text editor field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_rich_text_editor",
            data=response_data,
        )

    def add_field_nfc_reader(
        self,
        request: AddFieldNfcReaderRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_nfc_reader",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding NFC reader field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding NFC reader field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_nfc_reader",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added NFC reader field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_nfc_reader",
            data=response_data,
        )

    def add_field_number_input(
        self,
        request: AddFieldNumberInputRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_number_input",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding number input field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding number input field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_number_input",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added number input field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_number_input",
            data=response_data,
        )

    def add_field_pdf_viewer(
        self,
        request: AddFieldPdfViewerRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_pdf_viewer",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding PDF viewer field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding PDF viewer field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_pdf_viewer",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added PDF viewer field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_pdf_viewer",
            data=response_data,
        )

    def add_field_read_only_file(
        self,
        request: AddFieldReadOnlyFileRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_read_only_file",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding read-only file field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding read-only file field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_read_only_file",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added read-only file field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_read_only_file",
            data=response_data,
        )

    def add_field_read_only_text(
        self,
        request: AddFieldReadOnlyTextRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_read_only_text",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding read-only text field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding read-only text field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_read_only_text",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added read-only text field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_read_only_text",
            data=response_data,
        )

    def add_field_tags(
        self,
        request: AddFieldTagsRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_tags",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding tags field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding tags field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_tags",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added tags field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_tags",
            data=response_data,
        )

    def add_field_unique_sequential(
        self,
        request: AddFieldUniqueSequentialRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_unique_sequential",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding unique sequential field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding unique sequential field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_unique_sequential",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added unique sequential field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_unique_sequential",
            data=response_data,
        )

    def add_field_dropdown(
        self,
        request: AddFieldDropdownRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_dropdown",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding dropdown field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding dropdown field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_dropdown",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added dropdown field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_dropdown",
            data=response_data,
        )

    def add_field_radio(
        self,
        request: AddFieldRadioRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_radio",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding radio field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding radio field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_radio",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added radio field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_radio",
            data=response_data,
        )

    def add_field_url_input(
        self,
        request: AddFieldUrlInputRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_url_input",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding URL input field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding URL input field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_url_input",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added URL input field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_url_input",
            data=response_data,
        )

    def add_field_checkbox(
        self,
        request: AddFieldCheckboxRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_checkbox",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding checkbox field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding checkbox field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_checkbox",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added checkbox field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_checkbox",
            data=response_data,
        )

    def add_field_payment_gateway(
        self,
        request: AddFieldPaymentGatewayRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_payment_gateway",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding payment gateway field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding payment gateway field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_payment_gateway",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added payment gateway field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_payment_gateway",
            data=response_data,
        )

    def add_field_razorpay_payment_gateway(
        self,
        request: AddFieldRazorpayPaymentGatewayRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_razorpay_payment_gateway",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding Razorpay payment gateway field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding Razorpay payment gateway field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_razorpay_payment_gateway",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added Razorpay payment gateway field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_razorpay_payment_gateway",
            data=response_data,
        )

    def add_field_eazypay_payment_gateway(
        self,
        request: AddFieldEazypayPaymentGatewayRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_eazypay_payment_gateway",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding Eazypay payment gateway field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding Eazypay payment gateway field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_eazypay_payment_gateway",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added Eazypay payment gateway field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_eazypay_payment_gateway",
            data=response_data,
        )

    def add_field_paypal_payment_gateway(
        self,
        request: AddFieldPaypalPaymentGatewayRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_paypal_payment_gateway",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding PayPal payment gateway field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding PayPal payment gateway field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_paypal_payment_gateway",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added PayPal payment gateway field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_paypal_payment_gateway",
            data=response_data,
        )

    def add_field_stripe_payment_gateway(
        self,
        request: AddFieldStripePaymentGatewayRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_stripe_payment_gateway",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding Stripe payment gateway field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding Stripe payment gateway field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_stripe_payment_gateway",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added Stripe payment gateway field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_stripe_payment_gateway",
            data=response_data,
        )

    def add_field_button(
        self,
        request: AddFieldButtonRequest,
    ) -> FieldOperationResponse:
        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_button",
            )
        
        payload = request.to_json()
        
        logger.info(f"Adding button field to app_id: {request.app_id} with payload: {json.dumps(payload, indent=2)}")
        
        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )
        
        if not success:
            logger.error(f"Error adding button field: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=request.app_id,
                field_name=request.field_type,
                operation="add_field_button",
                data=response_data,
            )
        
        field_name = response_data.get("fieldName") if response_data else None
        
        return FieldOperationResponse(
            success=True,
            message=f"Successfully added button field to app {request.app_id}",
            app_id=request.app_id,
            field_name=field_name,
            operation="add_field_button",
            data=response_data,
        )

    def get_definition(
        self,
        app_id: str,
        language: str = "en",
    ) -> AppDefinitionResponse:
        try:
            request = GetAppDefinitionRequest(
                app_id=app_id,
                language=language,
            )
        except Exception as e:
            return AppDefinitionResponse(
                success=False,
                message=str(e),
                app_id=app_id,
            )

        params = {
            "appId": request.app_id,
            "language": request.language,
            "stripHtml": str(True).lower(),
            "includeTags": str(True).lower(),
        }

        logger.info(
            f"Getting app definition for app_id: {app_id} with params: {params}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="GET",
            endpoint="appdefinitionv2/getAppDefinition",
            params=params,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return AppDefinitionResponse(
                success=False, message=error_message, app_id=app_id
            )
        return AppDefinitionResponse(
            success=True,
            message="Successfully retrieved app definition",
            app_id=app_id,
            data=response_data,
        )

    def create_app(
        self,
        app_name: str,
        requesting_user_email_address: str,
        sections: List[Dict[str, Any]],
    ) -> AppCreationResponse:
        try:
            section_models = []
            for section_dict in sections:
                field_models = []
                for field_dict in section_dict.get("fields", []):
                    field_model = AppField(**field_dict)
                    field_models.append(field_model)

                section_model = AppSection(
                    section_name=section_dict["section_name"], fields=field_models
                )
                section_models.append(section_model)

            request = CreateAppRequest(
                app_name=app_name,
                requesting_user_email_address=requesting_user_email_address,
                sections=section_models,
            )
        except Exception as e:
            return AppCreationResponse(
                success=False,
                message=str(e),
                app_name=app_name,
                sections_created=len(sections),
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return AppCreationResponse(
                success=False,
                message=env_error,
                app_name=app_name,
                sections_created=len(sections),
            )

        sections_for_api = [section.to_dict() for section in request.sections]

        payload = {
            "appName": request.app_name.strip(),
            "requestingUserEmailAddress": str(
                request.requesting_user_email_address
            ).strip(),
            "sections": sections_for_api,
        }

        logger.info(f"Creating app with payload: {json.dumps(payload, indent=2)}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/createApp",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return AppCreationResponse(
                success=False,
                message=error_message,
                app_name=app_name,
                sections_created=len(sections),
            )

        app_id = response_data.get("appId") if response_data else None
        app_url = response_data.get("appUrl") if response_data else None

        return AppCreationResponse(
            success=True,
            message="App created successfully",
            app_id=app_id,
            app_name=app_name,
            sections_created=len(sections),
            data={"app_id": app_id, "app_url": app_url},
        )

    def add_field(
        self,
        app_id: str,
        section_index: int,
        field_index: int,
        field_type: str,
        label: Optional[str] = None,
        required: Optional[bool] = None,
        description: Optional[str] = None,
        block_width_percentage_desktop: Optional[int] = None,
        block_width_percentage_mobile: Optional[int] = None,
        display_condition: Optional[str] = None,
        retain_values: Optional[bool] = None,
        is_editable: Optional[bool] = None,
        editability_condition: Optional[str] = None,
        validation: Optional[str] = None,
        default_value: Optional[str] = None,
        options: Optional[List[str]] = None,
        style: Optional[str] = None,
        number_of_cols: Optional[int] = None,
        allowed_file_types: Optional[List[str]] = None,
        max_file_allowed: Optional[int] = None,
        image_quality: Optional[str] = None,
        image_text: Optional[str] = None,
        file_name_prefix: Optional[str] = None,
        formula: Optional[str] = None,
        hidden: Optional[bool] = None,
    ) -> FieldOperationResponse:
        try:
            request = AddFieldRequest(
                app_id=app_id,
                section_index=section_index,
                field_index=field_index,
                field_type=field_type,
                label=label,
                description=description,
                required=required,
                block_width_percentage_desktop=block_width_percentage_desktop,
                block_width_percentage_mobile=block_width_percentage_mobile,
                display_condition=display_condition,
                retain_values=retain_values,
                is_editable=is_editable,
                editability_condition=editability_condition,
                validation=validation,
                default_value=default_value,
                options=options,
                style=style,
                number_of_cols=number_of_cols,
                allowed_file_types=allowed_file_types,
                max_file_allowed=max_file_allowed,
                image_quality=image_quality,
                image_text=image_text,
                file_name_prefix=file_name_prefix,
                formula=formula,
                hidden=hidden,
            )
        except Exception as e:
            return FieldOperationResponse(
                success=False,
                message=str(e),
                app_id=app_id,
                field_name=field_type,
                operation="add_field",
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                field_name=field_type,
                operation="add_field",
            )

        payload = {
            "appId": request.app_id,
            "sectionIndex": request.section_index,
            "fieldIndex": request.field_index,
            "fieldType": request.field_type.value,
        }

        if request.description is not None:
            payload["description"] = request.description.strip()
        if request.required is not None:
            payload["required"] = request.required
        if request.label is not None:
            payload["label"] = request.label.strip()
        if request.block_width_percentage_desktop is not None:
            payload["blockWidthPercentageDesktop"] = (
                request.block_width_percentage_desktop
            )
        if request.block_width_percentage_mobile is not None:
            payload["blockWidthPercentageMobile"] = (
                request.block_width_percentage_mobile
            )
        if request.display_condition is not None:
            payload["displayCondition"] = request.display_condition.strip()
        if request.retain_values is not None:
            payload["retainValues"] = request.retain_values
        if request.is_editable is not None:
            payload["isEditable"] = request.is_editable
        if request.editability_condition is not None:
            payload["editabilityCondition"] = request.editability_condition.strip()
        if request.validation is not None:
            payload["validation"] = request.validation
        if request.default_value is not None and request.field_type == "singleLineText":
            payload["defaultValue"] = request.default_value.strip()
        if request.options is not None and request.field_type in [
            "singleSelector",
            "multiSelector",
            "dropDown",
        ]:
            payload["options"] = request.options
        if request.style is not None and request.field_type in [
            "singleSelector",
            "multiSelector",
        ]:
            payload["style"] = request.style
        if request.number_of_cols is not None and request.field_type in [
            "singleSelector",
            "multiSelector",
        ]:
            payload["numberOfCols"] = request.number_of_cols
        if request.allowed_file_types is not None and request.field_type == "file":
            payload["allowedFileTypes"] = request.allowed_file_types
        if request.max_file_allowed is not None and request.field_type == "file":
            payload["maxFileAllowed"] = request.max_file_allowed
        if request.image_quality is not None and request.field_type == "file":
            payload["imageQuality"] = request.image_quality
        if request.image_text is not None and request.field_type == "file":
            payload["imageText"] = request.image_text.strip()
        if request.file_name_prefix is not None and request.field_type == "file":
            payload["fileNamePrefix"] = request.file_name_prefix.strip()
        if request.formula is not None and request.field_type == "calculationsAndLogic":
            payload["formula"] = request.formula.strip()
        if request.hidden is not None and request.field_type == "formula":
            payload["hidden"] = request.hidden

        logger.info(f"Adding field to app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                field_name=field_type,
                operation="add_field",
                data=response_data,
            )

        field_name = response_data.get("fieldName") if response_data else None

        return FieldOperationResponse(
            success=True,
            message=f"Successfully added {field_type} field to app {app_id}",
            app_id=app_id,
            field_name=field_name,
            operation="add_field",
            data=response_data,
        )

    def add_section(
        self,
        app_id: str,
        section_index: int,
        page_index: int,
        section_name: str,
        description: Optional[str] = None,
        is_collapsible: Optional[bool] = None,
        is_collapsed_by_default: Optional[bool] = None,
    ) -> AddSectionResponse:
        """Add a new section to a Clappia app.

        Args:
            app_id: The ID of the app to add the section to
            section_index: Position where section will be inserted (0-based)
            page_index: Page index where section will be added
            section_name: Display name for the section
            description: Optional help text for the section
            is_collapsible: Allow users to expand/collapse section
            is_collapsed_by_default: Initial collapsed state

        Returns:
            AddSectionResponse: Response containing the result of the operation
        """
        try:
            request = AddSectionRequest(
                app_id=app_id,
                section_index=section_index,
                page_index=page_index,
                section_name=section_name,
                description=description,
                is_collapsible=is_collapsible,
                is_collapsed_by_default=is_collapsed_by_default,
            )
        except Exception as e:
            return AddSectionResponse(
                success=False,
                message=str(e),
                app_id=app_id,
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return AddSectionResponse(
                success=False,
                message=env_error,
                app_id=app_id,
            )

        payload = {
            "appId": request.app_id,
            "sectionIndex": request.section_index,
            "pageIndex": request.page_index,
            "sectionName": request.section_name,
        }

        if request.description is not None:
            payload["description"] = request.description.strip()
        if request.is_collapsible is not None:
            payload["isCollapsible"] = request.is_collapsible
        if request.is_collapsed_by_default is not None:
            payload["isCollapsedByDefault"] = request.is_collapsed_by_default

        logger.info(f"Adding section to app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addSection",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return AddSectionResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                data=response_data,
            )

        section_id = response_data.get("sectionId") if response_data else None
        section_index_response = response_data.get("sectionIndex") if response_data else None

        return AddSectionResponse(
            success=True,
            message=f"Successfully added section '{section_name}' to app {app_id}",
            app_id=app_id,
            section_id=section_id,
            section_index=section_index_response,
            section_name=section_name,
            data=response_data,
        )

    def update_section(
        self,
        app_id: str,
        section_index: int,
        page_index: int,
        section_name: Optional[str] = None,
        description: Optional[str] = None,
        is_collapsible: Optional[bool] = None,
        is_collapsed_by_default: Optional[bool] = None,
        keep_section_collapsed: Optional[bool] = None,
        allow_copy: Optional[bool] = None,
        max_number_of_copies: Optional[int] = None,
        add_section_text: Optional[str] = None,
        display_condition: Optional[str] = None,
    ) -> UpdateSectionResponse:
        """Update an existing section in a Clappia app.

        Args:
            app_id: The ID of the app containing the section
            section_index: Index of the section to update
            page_index: Page index of the section
            section_name: Display title of the section
            description: Help text or instructions for the section
            is_collapsible: Enable/disable expand/collapse functionality
            is_collapsed_by_default: Set initial display state
            keep_section_collapsed: Keep section collapsed
            allow_copy: Allow copying of the section
            max_number_of_copies: Maximum number of copies allowed
            add_section_text: Text for add section button
            display_condition: Display condition for the section

        Returns:
            UpdateSectionResponse: Response containing the result of the operation
        """
        try:
            request = UpdateSectionRequest(
                app_id=app_id,
                section_index=section_index,
                page_index=page_index,
                section_name=section_name,
                description=description,
                is_collapsible=is_collapsible,
                is_collapsed_by_default=is_collapsed_by_default,
                keep_section_collapsed=keep_section_collapsed,
                allow_copy=allow_copy,
                max_number_of_copies=max_number_of_copies,
                add_section_text=add_section_text,
                display_condition=display_condition,
            )
        except Exception as e:
            return UpdateSectionResponse(
                success=False,
                message=str(e),
                app_id=app_id,
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return UpdateSectionResponse(
                success=False,
                message=env_error,
                app_id=app_id,
            )

        payload = {
            "appId": request.app_id,
            "sectionIndex": request.section_index,
            "pageIndex": request.page_index,
        }

        if request.section_name is not None:
            payload["sectionName"] = request.section_name.strip()
        if request.description is not None:
            payload["description"] = request.description.strip()
        if request.is_collapsible is not None:
            payload["isCollapsible"] = request.is_collapsible
        if request.is_collapsed_by_default is not None:
            payload["isCollapsedByDefault"] = request.is_collapsed_by_default
        if request.keep_section_collapsed is not None:
            payload["keepSectionCollapsed"] = request.keep_section_collapsed
        if request.allow_copy is not None:
            payload["allowCopy"] = request.allow_copy
        if request.max_number_of_copies is not None:
            payload["maxNumberOfCopies"] = request.max_number_of_copies
        if request.add_section_text is not None:
            payload["addSectionText"] = request.add_section_text.strip()
        if request.display_condition is not None:
            payload["displayCondition"] = request.display_condition.strip()

        logger.info(f"Updating section in app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/updateSection",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return UpdateSectionResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                data=response_data,
            )

        section_index_response = response_data.get("sectionIndex") if response_data else None

        return UpdateSectionResponse(
            success=True,
            message=f"Successfully updated section at index {section_index} in app {app_id}",
            app_id=app_id,
            section_index=section_index_response,
            section_name=section_name,
            data=response_data,
        )

    def update_field(
        self,
        app_id: str,
        field_name: str,
        label: Optional[str] = None,
        description: Optional[str] = None,
        required: Optional[bool] = None,
        block_width_percentage_desktop: Optional[int] = None,
        block_width_percentage_mobile: Optional[int] = None,
        display_condition: Optional[str] = None,
        retain_values: Optional[bool] = None,
        is_editable: Optional[bool] = None,
        editability_condition: Optional[str] = None,
        validation: Optional[str] = None,
        default_value: Optional[str] = None,
        options: Optional[List[str]] = None,
        style: Optional[str] = None,
        number_of_cols: Optional[int] = None,
        allowed_file_types: Optional[List[str]] = None,
        max_file_allowed: Optional[int] = None,
        image_quality: Optional[str] = None,
        image_text: Optional[str] = None,
        file_name_prefix: Optional[str] = None,
        formula: Optional[str] = None,
        hidden: Optional[bool] = None,
    ) -> FieldOperationResponse:

        try:
            request = UpdateFieldRequest(
                app_id=app_id,
                field_name=field_name,
                label=label,
                description=description,
                required=required,
                block_width_percentage_desktop=block_width_percentage_desktop,
                block_width_percentage_mobile=block_width_percentage_mobile,
                display_condition=display_condition,
                retain_values=retain_values,
                is_editable=is_editable,
                editability_condition=editability_condition,
                validation=validation,
                default_value=default_value,
                options=options,
                style=style,
                number_of_cols=number_of_cols,
                allowed_file_types=allowed_file_types,
                max_file_allowed=max_file_allowed,
                image_quality=image_quality,
                image_text=image_text,
                file_name_prefix=file_name_prefix,
                formula=formula,
                hidden=hidden,
            )
        except Exception as e:
            return FieldOperationResponse(
                success=False,
                message=str(e),
                app_id=app_id,
                field_name=field_name,
                operation="update_field",
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return FieldOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                field_name=field_name,
                operation="update_field",
            )

        payload = {
            "appId": request.app_id,
            "fieldName": request.field_name,
        }

        updated_properties = []

        if request.label is not None:
            payload["label"] = request.label.strip()
            updated_properties.append("label")
        if request.required is not None:
            payload["required"] = request.required
            updated_properties.append("required")
        if request.description is not None:
            payload["description"] = request.description.strip()
            updated_properties.append("description")
        if request.block_width_percentage_desktop is not None:
            payload["blockWidthPercentageDesktop"] = (
                request.block_width_percentage_desktop
            )
            updated_properties.append("block_width_percentage_desktop")
        if request.block_width_percentage_mobile is not None:
            payload["blockWidthPercentageMobile"] = (
                request.block_width_percentage_mobile
            )
            updated_properties.append("block_width_percentage_mobile")
        if request.display_condition is not None:
            payload["displayCondition"] = request.display_condition.strip()
            updated_properties.append("display_condition")
        if request.retain_values is not None:
            payload["retainValues"] = request.retain_values
            updated_properties.append("retain_values")
        if request.is_editable is not None:
            payload["isEditable"] = request.is_editable
            updated_properties.append("is_editable")
        if request.editability_condition is not None:
            payload["editabilityCondition"] = request.editability_condition.strip()
            updated_properties.append("editability_condition")
        if request.validation is not None:
            payload["validation"] = request.validation
            updated_properties.append("validation")
        if request.default_value is not None:
            payload["defaultValue"] = request.default_value.strip()
            updated_properties.append("default_value")
        if request.options is not None:
            payload["options"] = request.options
            updated_properties.append("options")
        if request.style is not None:
            payload["style"] = request.style
            updated_properties.append("style")
        if request.number_of_cols is not None:
            payload["numberOfCols"] = request.number_of_cols
            updated_properties.append("number_of_cols")
        if request.allowed_file_types is not None:
            payload["allowedFileTypes"] = request.allowed_file_types
            updated_properties.append("allowed_file_types")
        if request.max_file_allowed is not None:
            payload["maxFileAllowed"] = request.max_file_allowed
            updated_properties.append("max_file_allowed")
        if request.image_quality is not None:
            payload["imageQuality"] = request.image_quality
            updated_properties.append("image_quality")
        if request.image_text is not None:
            payload["imageText"] = request.image_text.strip()
            updated_properties.append("image_text")
        if request.file_name_prefix is not None:
            payload["fileNamePrefix"] = request.file_name_prefix.strip()
            updated_properties.append("file_name_prefix")
        if request.formula is not None:
            payload["formula"] = request.formula.strip()
            updated_properties.append("formula")
        if request.hidden is not None:
            payload["hidden"] = request.hidden
            updated_properties.append("hidden")

        logger.info(
            f"Updating field '{field_name}' in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/updateField",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return FieldOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                field_name=field_name,
                operation="update_field",
                data=response_data,
            )

        return FieldOperationResponse(
            success=True,
            message=f"Successfully updated field '{field_name}' in app {app_id}",
            app_id=app_id,
            field_name=field_name,
            operation="update_field",
            data=response_data,
        )

    def add_page_break(
        self,
        app_id: str,
        page_index: int,
        section_index: int,
    ) -> PageBreakOperationResponse:
        """Add a page break to an app.

        Args:
            app_id: The app ID
            page_index: Page index where to add page break
            section_index: Section index where to add page break

        Returns:
            PageBreakOperationResponse: Response with operation result
        """
        try:
            request = AddPageBreakRequest(
                app_id=app_id,
                page_index=page_index,
                section_index=section_index,
            )
        except Exception as e:
            return PageBreakOperationResponse(
                success=False,
                message=str(e),
                app_id=app_id,
                page_index=page_index,
                operation="add_page_break",
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return PageBreakOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                page_index=page_index,
                operation="add_page_break",
            )

        payload = {
            "appId": request.app_id,
            "pageIndex": request.page_index,
            "sectionIndex": request.section_index,
        }

        logger.info(f"Adding page break to app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/addPageBreak",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return PageBreakOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                page_index=page_index,
                operation="add_page_break",
                data=response_data,
            )

        return PageBreakOperationResponse(
            success=True,
            message=f"Page break after Page with index {page_index} and after section with index {section_index} added successfully",
            app_id=app_id,
            page_index=page_index,
            operation="add_page_break",
            data=response_data,
        )

    def update_page(
        self,
        app_id: str,
        page_index: int,
        show_submit_button: Optional[bool] = None,
        previous_button_text: Optional[str] = None,
        next_button_text: Optional[str] = None,
    ) -> PageBreakOperationResponse:
        """Update page break settings in an app.

        Args:
            app_id: The app ID
            page_index: Page index to update
            show_submit_button: Show submit button
            previous_button_text: Previous button text
            next_button_text: Next button text

        Returns:
            PageBreakOperationResponse: Response with operation result
        """
        try:
            request = UpdatePageBreakRequest(
                app_id=app_id,
                page_index=page_index,
                show_submit_button=show_submit_button,
                previous_button_text=previous_button_text,
                next_button_text=next_button_text,
            )
        except Exception as e:
            return PageBreakOperationResponse(
                success=False,
                message=str(e),
                app_id=app_id,
                page_index=page_index,
                operation="update_page",
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return PageBreakOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                page_index=page_index,
                operation="update_page",
            )

        payload = {
            "appId": request.app_id,
            "pageIndex": request.page_index,
        }

        updated_properties = []

        if request.show_submit_button is not None:
            payload["showSubmitButton"] = request.show_submit_button
            updated_properties.append("show_submit_button")
        if request.previous_button_text is not None:
            payload["previousButtonText"] = request.previous_button_text.strip()
            updated_properties.append("previous_button_text")
        if request.next_button_text is not None:
            payload["nextButtonText"] = request.next_button_text.strip()
            updated_properties.append("next_button_text")

        logger.info(
            f"Updating page '{page_index}' in app_id: {app_id} with payload: {payload}"
        )

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/updatePageBreak",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return PageBreakOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                page_index=page_index,
                operation="update_page",
                data=response_data,
            )

        return PageBreakOperationResponse(
            success=True,
            message=f"Page at index {page_index} updated successfully",
            app_id=app_id,
            page_index=page_index,
            operation="update_page",
            data=response_data,
        )

    def reorder_section(
        self,
        app_id: str,
        source_section_index: int,
        target_section_index: int,
        source_page_index: Optional[int] = None,
        target_page_index: Optional[int] = None,
    ) -> SectionOperationResponse:
        """Reorder a section within an app.

        Args:
            app_id: The app ID
            source_section_index: Source section index
            target_section_index: Target section index
            source_page_index: Source page index (optional)
            target_page_index: Target page index (optional)

        Returns:
            SectionOperationResponse: Response containing section operation result
        """
        try:
            request = ReorderSectionRequest(
                app_id=app_id,
                source_section_index=source_section_index,
                target_section_index=target_section_index,
                source_page_index=source_page_index,
                target_page_index=target_page_index,
            )
        except Exception as e:
            return SectionOperationResponse(
                success=False,
                message=str(e),
                app_id=app_id,
                source_section_index=source_section_index,
                target_section_index=target_section_index,
                source_page_index=source_page_index,
                target_page_index=target_page_index,
                operation="reorder_section",
            )

        env_valid, env_error = self.api_utils.validate_environment()
        if not env_valid:
            return SectionOperationResponse(
                success=False,
                message=env_error,
                app_id=app_id,
                source_section_index=source_section_index,
                target_section_index=target_section_index,
                source_page_index=source_page_index,
                target_page_index=target_page_index,
                operation="reorder_section",
            )

        payload = {
            "appId": request.app_id,
            "sourceSectionIndex": request.source_section_index,
            "targetSectionIndex": request.target_section_index,
        }

        if request.source_page_index is not None:
            payload["sourcePageIndex"] = request.source_page_index
        if request.target_page_index is not None:
            payload["targetPageIndex"] = request.target_page_index

        logger.info(f"Reordering section in app_id: {app_id} with payload: {payload}")

        success, error_message, response_data = self.api_utils.make_request(
            method="POST",
            endpoint="appdefinitionv2/reorderSection",
            data=payload,
        )

        if not success:
            logger.error(f"Error: {error_message}")
            return SectionOperationResponse(
                success=False,
                message=error_message,
                app_id=app_id,
                source_section_index=source_section_index,
                target_section_index=target_section_index,
                source_page_index=source_page_index,
                target_page_index=target_page_index,
                operation="reorder_section",
                data=response_data,
            )

        return SectionOperationResponse(
            success=True,
            message="Section reordered successfully",
            app_id=app_id,
            source_section_index=source_section_index,
            target_section_index=target_section_index,
            source_page_index=source_page_index,
            target_page_index=target_page_index,
            operation="reorder_section",
            data=response_data,
        )
