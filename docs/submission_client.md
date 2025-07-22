# Submission Client Reference

This document provides a detailed reference for the `SubmissionClient` in the Clappia API Tools package.

## Overview

The `SubmissionClient` handles all operations related to submissions in Clappia apps, such as creating, editing, updating owners, changing status, retrieving submissions, and aggregating data.

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

---

### get_submissions

```python
def get_submissions(app_id: str, requesting_user_email_address: str, page_size: int = 10, filters: Optional[Filters] = None) -> str
```

Retrieves Clappia form submissions with optional filtering capabilities.

**Args:**

-  `app_id` (str): Application ID in uppercase letters and numbers format (e.g., MFX093412).
-  `requesting_user_email_address` (str): Email address of the user requesting the submissions. Must be a valid email format.
-  `page_size` (int, optional): Number of results to retrieve (1-1000, default: 10).
-  `filters` (Optional[Filters], optional): Filter conditions using the Filters class for advanced querying.

**Returns:**

-  `str`: JSON string with submission records and metadata, or error message if the request fails.

**Notes:**

-  Page size is limited to 1000 records per request for performance.
-  Filters support various operators for flexible querying.
-  The response includes submission count and full submission data.

---

### get_submissions_aggregation

```python
def get_submissions_aggregation(app_id: str, dimensions: List[Dimension] = None, aggregation_dimensions: List[AggregationDimension] = None, x_axis_labels: List[str] = None, requesting_user_email_address: str = "dev@clappia.com", forward: bool = True, page_size: int = 1000, filters: Optional[Filters] = None) -> str
```

Aggregates Clappia submission data for analytics and reporting.

**Args:**

-  `app_id` (str): Application ID in uppercase letters and numbers format (e.g., MFX093412).
-  `dimensions` (List[Dimension], optional): Fields to group by for analysis.
-  `aggregation_dimensions` (List[AggregationDimension], optional): Calculations to perform (count, sum, average, etc.).
-  `x_axis_labels` (List[str], optional): Output column labels for the aggregated data.
-  `requesting_user_email_address` (str, optional): User email. Defaults to "dev@clappia.com".
-  `forward` (bool, optional): Pagination direction. Defaults to True.
-  `page_size` (int, optional): Max results (1-1000). Defaults to 1000.
-  `filters` (Optional[Filters], optional): Filter conditions for the aggregation.

**Returns:**

-  `str`: JSON string with tabular data or error message.

**Notes:**

-  At least one dimension or aggregation_dimension is required.
-  The response format is a 2D array where the first row contains headers and subsequent rows contain data.

### get_submissions_in_excel

```python
def get_submissions_in_excel(app_id: str, requesting_user_email_address: str, filters: Optional[SubmissionFilters] = None, field_names: Optional[List[str]] = None, format: str = "Excel") -> SubmissionsExcelResponse
```

Exports submissions to Excel or CSV format with optional filtering and field selection.

**Parameters:**

-  `app_id` (str): The Clappia app ID
-  `requesting_user_email_address` (str): Email of the requesting user
-  `filters` (Optional[SubmissionFilters]): Optional filters to apply to the export
-  `field_names` (Optional[List[str]]): List of field names to include in the export
-  `format` (str): Export format, either "Excel" or "Csv" (default: "Excel")

**Returns:**

-  `SubmissionsExcelResponse`: Response containing either a download URL or confirmation that the file was sent via email

**Example:**

```python
from clappia_api_tools.client.submission_client import SubmissionClient

client = SubmissionClient()

# Export all submissions to Excel
response = client.get_submissions_in_excel(
    app_id="APP123",
    requesting_user_email_address="user@example.com",
    format="Excel"
)

if response.success:
    if response.url:
        print(f"Download URL: {response.url}")
    else:
        print(f"File sent to: {response.requesting_user_email_address}")
```

**Response Handling:**

-  If the API returns status code 202, the file is sent via email and the response includes the email address
-  Otherwise, a download URL is provided for immediate file access

## Filter Models

### Filters

The `Filters` class allows you to create complex queries for filtering submissions:

```python
from clappia_api_tools._models.model import Condition, Query, QueryGroup, Filters
from clappia_api_tools._enums.enums import FilterOperator, FilterKeyType

# Create a condition
condition = Condition(
    operator=FilterOperator.EQ.value,
    filterKeyType=FilterKeyType.STANDARD.value,
    key="$status",
    value="approved"
)

# Create a query with the condition
query = Query(conditions=[condition])

# Create a query group
query_group = QueryGroup(queries=[query])

# Create filters
filters = Filters(queries=[query_group])
```

### Available Filter Operators

-  `CONTAINS`: Check if field contains a value
-  `NOT_IN`: Check if field is not in a list
-  `EQ`: Equal to
-  `NEQ`: Not equal to
-  `EMPTY`: Field is empty
-  `NON_EMPTY`: Field is not empty
-  `STARTS_WITH`: Field starts with a value
-  `BETWEEN`: Field is between two values
-  `GT`: Greater than
-  `LT`: Less than
-  `GTE`: Greater than or equal to
-  `LTE`: Less than or equal to

### Standard Fields

The following standard fields are available for filtering:

-  `$submissionId`: Submission ID
-  `$owner`: Submission owner
-  `$status`: Submission status
-  `$createdAt`: Creation date
-  `$updatedAt`: Last update date
-  `$state`: Submission state

## Aggregation Models

### Dimension

The `Dimension` class defines how to group data:

```python
from clappia_api_tools._models.model import Dimension

dimension = Dimension(
    fieldName="region",
    label="Region",
    dataType=fieldType
    dimensionType="CUSTOM"
)
```

### AggregationDimension

The `AggregationDimension` class defines calculations to perform:

```python
from clappia_api_tools._models.model import AggregationDimension, AggregationOperand

# Count aggregation
count_agg = AggregationDimension(type=AggregationType.COUNT.value)

# Sum aggregation
sum_agg = AggregationDimension(
    type=AggregationType.SUM.value,
    operand=AggregationOperand(
        fieldName="sales_amount",
        label="Total Sales",
        dataType=fieldType
        dimensionType="CUSTOM"
    )
)
```

### Available Aggregation Types

-  `count`: Count of records
-  `sum`: Sum of numeric values
-  `average`: Average of numeric values
-  `minimum`: Minimum value
-  `maximum`: Maximum value
-  `unique`: Count of unique values

## Usage Example

```python
from clappia_api_tools.client.submission_client import SubmissionClient
from clappia_api_tools._models.model import Condition, Query, QueryGroup, Filters, Dimension, AggregationDimension, AggregationOperand
from clappia_api_tools._enums.enums import FilterOperator, FilterKeyType, AggregationType

client = SubmissionClient(
    api_key="your-api-key",
    base_url="https://api.clappia.com",
    workplace_id="your-workplace-id"
)

# Create a submission
result = client.create_submission(
    app_id="MFX093412",
    data={"employee_name": "John Doe", "department": "Engineering"},
    requesting_user_email_address="user@example.com"
)
print(result)

# Get submissions with filters
condition = Condition(
    operator=FilterOperator.EQ.value,
    filterKeyType=FilterKeyType.STANDARD.value,
    key="$status",
    value="approved"
)
query = Query(conditions=[condition])
query_group = QueryGroup(queries=[query])
filters = Filters(queries=[query_group])

result = client.get_submissions(
    app_id="MFX093412",
    requesting_user_email_address="user@example.com",
    page_size=50,
    filters=filters
)
print(result)

# Get aggregated data
region_dimension = Dimension(
    fieldName="region",
    label="Region",
    dataType=fieldType
    dimensionType="CUSTOM"
)

count_aggregation = AggregationDimension(type=AggregationType.COUNT.value)

result = client.get_submissions_aggregation(
    app_id="MFX093412",
    dimensions=[region_dimension],
    aggregation_dimensions=[count_aggregation],
    x_axis_labels=["Region", "Count"],
    requesting_user_email_address="user@example.com"
)
print(result)
```
