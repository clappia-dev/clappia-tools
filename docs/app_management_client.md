# App Management Client Reference

This document provides a detailed reference for the `AppManagementClient` in the Clappia API Tools package.

## Overview

The `AppManagementClient` handles operations related to managing app structure, such as updating fields and sections.

## Import

```python
from clappia_api_tools.client.app_management_client import AppManagementClient
```

## Initialization

Instantiate `AppManagementClient` directly with the required parameters:

```python
client = AppManagementClient(
    api_key="your-api-key",
    base_url="https://api.clappia.com",
    workplace_id="your-workplace-id"
)
```

## Methods

### create_app

```python
def create_app(app_name: str, requesting_user_email_address: str, sections: List[Dict[str, Any]]) -> str
```
Create a new Clappia application with specified sections and fields.

**Args:**
- `app_name` (str): Name of the new application (e.g., "Employee Survey"). Minimum 10 characters.
- `requesting_user_email_address` (str): Email address of the user creating the app (becomes the app owner).
- `sections` (List[Dict[str, Any]]): List of Section objects defining the app structure. Each section contains fields with specific types and properties.

**Returns:**
- `str`: Success message with app ID and URL, or error message if the request fails.

---

### add_field

```python
def add_field(app_id: str, requesting_user_email_address: str, section_index: int, field_index: int, field_type: str, label: Optional[str] = None, required: Optional[bool] = None, description: Optional[str] = None, block_width_percentage_desktop: Optional[int] = None, block_width_percentage_mobile: Optional[int] = None, display_condition: Optional[str] = None, retain_values: Optional[bool] = None, is_editable: Optional[bool] = None, editability_condition: Optional[str] = None, validation: Optional[str] = None, default_value: Optional[str] = None, options: Optional[List[str]] = None, style: Optional[str] = None, number_of_cols: Optional[int] = None, allowed_file_types: Optional[List[str]] = None, max_file_allowed: Optional[int] = None, image_quality: Optional[str] = None, image_text: Optional[str] = None, file_name_prefix: Optional[str] = None, formula: Optional[str] = None, hidden: Optional[bool] = None) -> str
```
Add a new field to an existing Clappia application at a specific position.

**Args:**
- `app_id` (str): Application ID (e.g., "MFX093412").
- `requesting_user_email_address` (str): Email address of the user adding the field.
- `section_index` (int): Index of the section to add the field to (starts from 0).
- `field_index` (int): Position within the section for the new field (starts from 0).
- `field_type` (str): Type of field (e.g., "singleLineText", "singleSelector").
- `label` (Optional[str]): Display label for the field.
- `required` (Optional[bool]): Whether the field is required.
- `description` (Optional[str]): Field description or help text.
- `block_width_percentage_desktop` (Optional[int]): Width percentage on desktop.
- `block_width_percentage_mobile` (Optional[int]): Width percentage on mobile.
- `display_condition` (Optional[str]): Condition for when to show the field.
- `retain_values` (Optional[bool]): Whether to retain values when field is hidden.
- `is_editable` (Optional[bool]): Whether the field can be edited.
- `editability_condition` (Optional[str]): Condition for when field is editable.
- `validation` (Optional[str]): Validation type.
- `default_value` (Optional[str]): Default value for the field.
- `options` (Optional[List[str]]): List of options for selector fields.
- `style` (Optional[str]): Style for selector fields.
- `number_of_cols` (Optional[int]): Number of columns for selector fields.
- `allowed_file_types` (Optional[List[str]]): List of allowed file types for file fields.
- `max_file_allowed` (Optional[int]): Maximum files allowed.
- `image_quality` (Optional[str]): Image quality for file fields.
- `image_text` (Optional[str]): Text overlay for image fields.
- `file_name_prefix` (Optional[str]): Prefix for uploaded file names.
- `formula` (Optional[str]): Formula for calculation fields.
- `hidden` (Optional[bool]): Whether the field is hidden.

**Returns:**
- `str`: Success message with generated field name or error message if the request fails.

---

### update_field

```python
def update_field(app_id: str, requesting_user_email_address: str, field_name: str, label: Optional[str] = None, description: Optional[str] = None, required: Optional[bool] = None, block_width_percentage_desktop: Optional[int] = None, block_width_percentage_mobile: Optional[int] = None, display_condition: Optional[str] = None, retain_values: Optional[bool] = None, is_editable: Optional[bool] = None, editability_condition: Optional[str] = None, validation: Optional[str] = None, default_value: Optional[str] = None, options: Optional[List[str]] = None, style: Optional[str] = None, number_of_cols: Optional[int] = None, allowed_file_types: Optional[List[str]] = None, max_file_allowed: Optional[int] = None, image_quality: Optional[str] = None, image_text: Optional[str] = None, file_name_prefix: Optional[str] = None, formula: Optional[str] = None, hidden: Optional[bool] = None) -> str
```
Update an existing field in a Clappia application.

**Args:**
- `app_id` (str): Application ID (e.g., "MFX093412").
- `requesting_user_email_address` (str): Email address of the user updating the field.
- `field_name` (str): Name of the field to update.
- `label` (Optional[str]): Display label for the field.
- `description` (Optional[str]): Field description or help text.
- `required` (Optional[bool]): Whether the field is required.
- `block_width_percentage_desktop` (Optional[int]): Width percentage on desktop.
- `block_width_percentage_mobile` (Optional[int]): Width percentage on mobile.
- `display_condition` (Optional[str]): Condition for when to show the field.
- `retain_values` (Optional[bool]): Whether to retain values when field is hidden.
- `is_editable` (Optional[bool]): Whether the field can be edited.
- `editability_condition` (Optional[str]): Condition for when field is editable.
- `validation` (Optional[str]): Validation type.
- `default_value` (Optional[str]): Default value for the field.
- `options` (Optional[List[str]]): List of options for selector fields.
- `style` (Optional[str]): Style for selector fields.
- `number_of_cols` (Optional[int]): Number of columns for selector fields.
- `allowed_file_types` (Optional[List[str]]): List of allowed file types for file fields.
- `max_file_allowed` (Optional[int]): Maximum files allowed.
- `image_quality` (Optional[str]): Image quality for file fields.
- `image_text` (Optional[str]): Text overlay for image fields.
- `file_name_prefix` (Optional[str]): Prefix for uploaded file names.
- `formula` (Optional[str]): Formula for calculation fields.
- `hidden` (Optional[bool]): Whether the field is hidden.

**Returns:**
- `str`: Success message or error message if the request fails.

## Usage Example

```python
from clappia_api_tools.client.app_management_client import AppManagementClient

client = AppManagementClient(
    api_key="your-api-key",
    base_url="https://api.clappia.com",
    workplace_id="your-workplace-id"
)

# Example usage for app management methods
# result = client.create_app(...)
# print(result)
```
