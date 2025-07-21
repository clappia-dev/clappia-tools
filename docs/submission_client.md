# Submission Client Reference

This document provides a detailed reference for the `SubmissionClient` in the Clappia API Tools package.

## Overview

The `SubmissionClient` handles all operations related to submissions in Clappia apps, such as creating, editing, updating owners, and changing status.

## Import

```python
from clappia_api_tools.client.submission_client import SubmissionClient
```

## Initialization

Instantiate `SubmissionClient` directly with the required parameters:

```python
client = SubmissionClient(
    api_key="your-api-key",
    base_url="https://api.clappia.com",
    workplace_id="your-workplace-id"
)
```

## Methods

### create_submission

```python
def create_submission(app_id: str, data: Dict[str, Any], requesting_user_email_address: str) -> str
```

Creates a new submission in a Clappia application with specified field data.

**Args:**

-  `app_id` (str): Application ID in uppercase letters and numbers format (e.g., MFX093412). Specifies which Clappia app to create the submission in.
-  `data` (Dict[str, Any]): Dictionary of field data to submit. Keys should match field names from the app definition, values should match expected field types. Example: `{ "employee_name": "John Doe", "department": "Engineering" }`.
-  `requesting_user_email_address` (str): Email address of the user creating the submission. Must be a valid email format.

**Returns:**

-  `str`: Formatted response with submission details and status.

---

### edit_submission

```python
def edit_submission(app_id: str, submission_id: str, data: Dict[str, Any], requesting_user_email_address: str) -> str
```

Edits an existing Clappia submission by updating specified field values.

**Args:**

-  `app_id` (str): Application ID in uppercase letters and numbers format (e.g., MFX093412).
-  `submission_id` (str): Unique identifier of the submission to update (e.g., HGO51464561).
-  `data` (Dict[str, Any]): Dictionary of field data to update. Only specified fields will be updated.
-  `requesting_user_email_address` (str): Email address of the user requesting the edit. Must be a valid email format.

**Returns:**

-  `str`: Formatted response with edit details and status.

---

### update_owners

```python
def update_owners(app_id: str, submission_id: str, requesting_user_email_address: str, email_ids: List[str]) -> str
```

Updates the ownership of a Clappia submission by adding new owners to share access.

**Args:**

-  `app_id` (str): Application ID in uppercase letters and numbers format (e.g., MFX093412).
-  `submission_id` (str): Unique identifier of the submission to update (e.g., HGO51464561).
-  `requesting_user_email_address` (str): Email address of the user making the ownership change. Must be a valid email format.
-  `email_ids` (List[str]): List of email addresses to add as new owners. Each email must be valid.

**Returns:**

-  `str`: Formatted response with update details and status.

---

### update_status

```python
def update_status(app_id: str, submission_id: str, requesting_user_email_address: str, status_name: str, comments: str) -> str
```

Updates the status of a Clappia submission to track workflow progress and approvals.

**Args:**

-  `app_id` (str): Application ID in uppercase letters and numbers format (e.g., MFX093412).
-  `submission_id` (str): Unique identifier of the submission to update (e.g., HGO51464561).
-  `requesting_user_email_address` (str): Email address of the user making the status change. Must be a valid email format.
-  `status_name` (str): Name of the new status to apply to the submission.
-  `comments` (str): Optional comments to include with the status change.

**Returns:**

-  `str`: Formatted response with update details and status.

## Usage Example

```python
from clappia_api_tools.client.submission_client import SubmissionClient

client = SubmissionClient(
    api_key="your-api-key",
    base_url="https://api.clappia.com",
    workplace_id="your-workplace-id"
)

result = client.create_submission(
    app_id="MFX093412",
    data={"employee_name": "John Doe", "department": "Engineering"},
    requesting_user_email_address="user@example.com"
)
print(result)
```
