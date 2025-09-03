# Workflow Definition Client

The `WorkflowDefinitionClient` provides a comprehensive interface for managing workflow definitions in Clappia. This client enables you to retrieve, create, modify, and manage workflow steps programmatically.

## Overview

Workflows in Clappia are automated processes that trigger specific actions when certain events occur (like submission creation, updates, etc.). The WorkflowDefinitionClient allows you to:

-  Retrieve existing workflow definitions
-  Add new workflow steps
-  Update workflow step configurations
-  Reorder workflow steps

## Initialization

```python
from clappia_api_tools.client.workflow_definition_client import WorkflowDefinitionClient

client = WorkflowDefinitionClient(
    api_key="your-api-key",
    base_url="https://api.clappia.com",
)
```

## Available Methods

### Get Schema

Retrieve the schema for workflow definitions. This provides information about the structure and configuration options available for workflows.

```python
# Get schema for a specific node type
result = client.get_schema(node_type="Email")

if result.success:
    print(f"Schema retrieved: {result.message}")
    print(f"Schema data: {result.data}")
else:
    print(f"Error: {result.message}")
```

**Parameters:**

-  `node_type` (str): Node type to filter the schema (e.g., "Email", "SMS", "Slack", etc.)

**Returns:**

-  `WorkflowResponse`: Response containing the workflow schema data

### Get Workflow Definition

Retrieve the complete workflow definition for a specific app and trigger type.

```python
result = client.get_workflow(
    app_id="MFX093412",
    trigger_type="submissionCreated",
)

if result.success:
    print(f"Workflow retrieved: {result.message}")
    print(f"Number of steps: {len(result.data.get('steps', []))}")
else:
    print(f"Error: {result.message}")
```

**Parameters:**

-  `app_id` (str): App Id
-  `trigger_type` (str): The trigger type for the workflow

**Valid Trigger Types:**

-  `submissionCreated`
-  `submissionEdited`
-  `submissionStatusEdited`
-  `schedule`

### Add Workflow Step

Add a new workflow step to an existing workflow.

```python
result = client.add_workflow_step(
    app_id="MFX093412",
    trigger_type="submissionCreated",
    node_type="Email",
    parent_variable_name="Start"  # Optional, defaults to "Start"
)

if result.success:
    print(f"Step added: {result.message}")
else:
    print(f"Error: {result.message}")
```

**Parameters:**

-  `app_id` (str): App Id
-  `trigger_type` (str): The trigger type for the workflow
-  `node_type` (str): Type of workflow node to add
-  `parent_variable_name` (str, optional): Parent workflow step variable name (default: "Start")

**Valid Node Types:**

-  `Email` - Send email notifications
-  `Slack` - Send Slack notifications
-  `WhatsApp` - Send WhatsApp messages
-  `Mobile` - Send mobile push notifications
-  `SMS` - Send SMS messages
-  `Sync` - Synchronize data
-  `Pass` - Pass-through node
-  `CreateClappiaAppSubmission` - Create submissions in other apps
-  `EditClappiaAppSubmission` - Edit submissions in other apps
-  `FindClappiaAppSubmission` - Find submissions in other apps
-  `DeleteClappiaAppSubmission` - Delete submissions in other apps

```

**Parameters:**

-  `app_id` (str): App Id
-  `trigger_type` (str): The trigger type for the workflow
-  `step_variable_name` (str): Variable name of the workflow step to update

### Update Workflow Step

Update the configuration of an existing workflow step.

```python
update_data = {
    "new_variable_name": "updated_email_notification",
    "email_subject": "Updated Subject",
    "email_body": "Updated email body content"
}

result = client.update_workflow_step(
    app_id="MFX093412",
    trigger_type="submissionCreated",
    step_variable_name="email_notification",
    update_data=update_data
)

if result.success:
    print(f"Step updated: {result.message}")
else:
    print(f"Error: {result.message}")
```

**Parameters:**

-  `app_id` (str): App Id
-  `trigger_type` (str): The trigger type for the workflow
-  `step_variable_name` (str): Variable name of the workflow step to update
-  `update_data` (dict): Dictionary containing the fields to update

### Reorder Workflow Step

Move a workflow step to a different position in the workflow by changing its parent.

```python
result = client.reorder_workflow_step(
    app_id="MFX093412",
    trigger_type="submissionCreated",
    step_variable_name="email_notification",
    parent_variable_name="validation_step",
)

if result.success:
    print(f"Step reordered: {result.message}")
else:
    print(f"Error: {result.message}")
```

**Parameters:**

-  `app_id` (str): App Id
-  `trigger_type` (str): The trigger type for the workflow
-  `step_variable_name` (str): Variable name of the workflow step to move
-  `parent_variable_name` (str): Variable name of the new parent workflow step

## Response Models

### WorkflowResponse

Returned by `get_workflow()` method:

```python
class WorkflowResponse(BaseResponse):
    app_id: str
    trigger_definition: Optional[WorkflowTriggerDefinition]
    steps: Optional[List[WorkflowStep]]
    last_updated_by: Optional[WorkflowLastUpdatedBy]
    last_updated_at: Optional[str]
```

### WorkflowStepResponse

Returned by workflow modification methods:

```python
class WorkflowStepResponse(BaseResponse):
    app_id: str
    trigger_type: str
    step_variable_name: Optional[str]
    operation: str
    parent_variable_name: Optional[str]
```

## Error Handling

All methods return response objects with consistent error handling:

```python
result = client.get_workflow(
    app_id="INVALID_ID",
    trigger_type="submissionCreated",
)

if not result.success:
    print(f"Error: {result.message}")
    # Handle error appropriately
```

## Complete Example

Here's a complete example showing how to manage a workflow:

```python
from clappia_api_tools.client.workflow_definition_client import WorkflowDefinitionClient

# Initialize client
client = WorkflowDefinitionClient(
    api_key="your-api-key",
    base_url="https://api.clappia.com",
)

# Get existing workflow
workflow = client.get_workflow(
    app_id="MFX093412",
    trigger_type="submissionCreated",
)

if workflow.success:
    print(f"Found workflow with {len(workflow.data.get('steps', []))} steps")

    # Add an email notification step
    add_result = client.add_workflow_step(
        app_id="MFX093412",
        trigger_type="submissionCreated",
        node_type="Email",
    )

    if add_result.success:
        print("Email step added successfully")

        # Update the email step configuration
        update_data = {
            "email_subject": "New Submission Created",
            "email_body": "A new submission has been created in the system."
        }

        update_result = client.update_workflow_step(
            app_id="MFX093412",
            trigger_type="submissionCreated",
            step_variable_name="email_notification",  # Generated variable name
            update_data=update_data
        )

        if update_result.success:
            print("Email step updated successfully")
        else:
            print(f"Failed to update step: {update_result.message}")
    else:
        print(f"Failed to add step: {add_result.message}")
else:
    print(f"Failed to get workflow: {workflow.message}")
```

## Best Practices

1. **Always check response success**: Verify the `success` field before proceeding
2. **Handle errors gracefully**: Implement proper error handling for failed operations
3. **Use descriptive variable names**: Choose meaningful names for workflow steps
4. **Test in development**: Test workflow changes in a development environment first
5. **Monitor workflow execution**: Keep track of workflow performance and errors

## Validation

The client includes comprehensive validation for:

-  App ID format (uppercase letters and numbers only)
-  Valid trigger types
-  Valid node types
-  Required field validation
-  Email format validation

Invalid inputs will return descriptive error messages to help identify and fix issues.
