from unittest.mock import patch, Mock
from clappia_tools._tools.create_submission import create_clappia_submission
from clappia_tools._tools.edit_submission import edit_clappia_submission
from clappia_tools._tools.get_definition import get_app_definition
from clappia_tools._tools.update_submission_owners import update_clappia_submission_owners
from clappia_tools._tools.update_submission_status import update_clappia_submission_status

class TestToolsIntegration:
    @patch("clappia_tools._tools.create_submission.ClappiaClient")
    def test_create_submission_tool(self, mock_client_class):
        # Setup mock
        mock_client = Mock()
        mock_client.create_submission.return_value = (
            "Success: Created submission TEST123"
        )
        mock_client_class.return_value = mock_client

        # Call tool
        result = create_clappia_submission(
            "MFX093412",
            {"name": "Test User"},
            "test@example.com",
        )

        # Verify
        assert "Success: Created submission TEST123" in result
        mock_client.create_submission.assert_called_once_with(
            "MFX093412", {"name": "Test User"}, "test@example.com"
        )

    @patch("clappia_tools._tools.get_definition.ClappiaClient")
    def test_get_definition_tool(self, mock_client_class):
        # Setup mock
        mock_client = Mock()
        mock_client.get_app_definition.return_value = "App definition for MFX093412"
        mock_client_class.return_value = mock_client

        # Call tool
        result = get_app_definition("MFX093412")

        # Verify
        assert "App definition for MFX093412" in result
        mock_client.get_app_definition.assert_called_once_with(
            "MFX093412", "en", True, True
        )

    @patch("clappia_tools._tools.edit_submission.ClappiaClient")
    def test_edit_submission_tool(self, mock_client_class):
        # Setup mock
        mock_client = Mock()
        mock_client.edit_submission.return_value = "Success: Edited submission TEST123"
        mock_client_class.return_value = mock_client

        # Call tool
        result = edit_clappia_submission(
            "MFX093412",
            "HGO51464561",
            {"name": "Test User"},
            "test@example.com",
        )

        # Verify
        assert "Success: Edited submission TEST123" in result
        mock_client.edit_submission.assert_called_once_with(
            "MFX093412", "HGO51464561", {"name": "Test User"}, "test@example.com"
        )

    @patch("clappia_tools._tools.update_submission_owners.ClappiaClient")
    def test_update_submission_owners_tool(self, mock_client_class):
        # Setup mock
        mock_client = Mock()
        mock_client.update_submission_owners.return_value = (
            "Success: Updated submission owners for TEST123"
        )
        mock_client_class.return_value = mock_client

        # Call tool
        result = update_clappia_submission_owners(
            "MFX093412",
            "HGO51464561",
            "admin@example.com",
            ["user1@company.com", "user2@company.com"],
        )
        assert "Success: Updated submission owners for TEST123" in result
        mock_client.update_submission_owners.assert_called_once_with(
            "MFX093412",
            "HGO51464561",
            "admin@example.com",
            ["user1@company.com", "user2@company.com"],
        )

    @patch("clappia_tools._tools.update_submission_status.ClappiaClient")
    def test_update_submission_status_tool(self, mock_client_class):
        # Setup mock
        mock_client = Mock()
        mock_client.update_submission_status.return_value = (
            "Success: Updated submission status for TEST123"
        )
        mock_client_class.return_value = mock_client

        # Call tool
        result = update_clappia_submission_status(
            "MFX093412",
            "HGO51464561",
            "admin@example.com",
            "Approved", 
            "Reviewed and approved by manager",
        )

        assert "Success: Updated submission status for TEST123" in result
        mock_client.update_submission_status.assert_called_once_with(
            "MFX093412",
            "HGO51464561",
            "admin@example.com",
            "Approved",
            "Reviewed and approved by manager",
        )
