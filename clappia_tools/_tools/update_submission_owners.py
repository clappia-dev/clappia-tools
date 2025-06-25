from typing import List
from clappia_tools.client.clappia_client import ClappiaClient


def update_clappia_submission_owners(
    app_id: str,
    submission_id: str,
    requesting_user_email_address: str,
    email_ids: List[str],
) -> str:
    """Updates the ownership of a Clappia submission by adding new owners to share access.

    Modifies submission ownership to include additional users who can view and edit the submission.
    Use this to collaborate on submissions, delegate work, or transfer ownership.

    Args:
        app_id: Application ID in uppercase letters and numbers format (e.g., MFX093412). Use this to specify which Clappia app contains the submission.
        submission_id: Unique identifier of the submission to update (e.g., HGO51464561). This identifies the specific submission record to modify.
        requesting_user_email_address: Email address of the user making the ownership change. This user must have permission to modify the submission. Must be a valid email format.
        email_ids: List of email addresses to add as new owners. Each email must be valid and the users should have access to the app. Example: ["user1@company.com", "user2@company.com"]. Invalid emails will be skipped with a warning.

    Returns:
        str: Formatted response with update details and status
    """
    client = ClappiaClient()
    return client.update_submission_owners(app_id, submission_id, requesting_user_email_address, email_ids) 