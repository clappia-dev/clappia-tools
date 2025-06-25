from typing import Dict, Any
from clappia_tools.client.clappia_client import ClappiaClient


def update_clappia_submission_status(
    app_id: str,
    submission_id: str,
    requesting_user_email_address: str,
    status_name: str,
    comments: str,
) -> str:
    """Updates the status of a Clappia submission to track workflow progress and approvals.

    Changes the submission status to indicate current stage in workflow (e.g., pending, approved, rejected).
    Use this to manage approval workflows, track processing stages, or update submission lifecycle.

    Args:
        app_id: Application ID in uppercase letters and numbers format (e.g., MFX093412). Use this to specify which Clappia app contains the submission.
        submission_id: Unique identifier of the submission to update (e.g., HGO51464561). This identifies the specific submission record to modify.
        requesting_user_email_address: Email address of the user making the status change. This user must have permission to modify the submission. Must be a valid email format.
        status_name: Name of the new status to apply to the submission.
        comments: Optional comments to include with the status change.

    Returns:
        str: Formatted response with update details and status
    """
    client = ClappiaClient()
    return client.update_submission_status(app_id, submission_id, requesting_user_email_address, status_name, comments) 