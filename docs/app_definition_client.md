# App Definition Client

The `AppDefinitionClient` provides methods to manage Clappia app definitions, including creating apps, adding fields, and updating field properties.

## Methods

### `get_definition(app_id, language="en", strip_html=True, include_tags=True)`

Retrieves the complete definition of a Clappia app.

**Parameters:**

-  `app_id` (str): The Clappia app ID
-  `language` (str): Language code (default: "en")
-  `strip_html` (bool): Remove HTML formatting (default: True)
-  `include_tags` (bool): Include metadata tags (default: True)

**Returns:**

-  `AppDefinitionResponse`: Response containing app definition data

**Example:**

```python
response = client.get_definition("APP123")
if response.success:
    print(f"App: {response.data['app_name']}")
    print(f"Fields: {response.data['field_count']}")
```

### `create_app(app_name, requesting_user_email_address, sections)`

Creates a new Clappia app with specified sections and fields.

**Parameters:**

-  `app_name` (str): Name of the app to create
-  `requesting_user_email_address` (str): Email of requesting user
-  `sections` (List[Dict]): Array of sections with fields

**Returns:**

-  `AppCreationResponse`: Response containing app creation result

**Example:**

```python
sections = [
    {
        "section_name": "Basic Info",
        "fields": [
            {
                "field_type": "singleLineText",
                "label": "Name"
            }
        ]
    }
]

response = client.create_app("My App", "user@example.com", sections)
if response.success:
    print(f"App created with ID: {response.app_id}")
```

### `add_field(app_id, requesting_user_email_address, section_index, field_index, field_type, **kwargs)`

Adds a new field to an existing Clappia app.

**Parameters:**

-  `app_id` (str): The app ID
-  `requesting_user_email_address` (str): Email of requesting user
-  `section_index` (int): Section index where to add the field
-  `field_index` (int): Field index within the section
-  `field_type` (str): Type of field to add
-  `**kwargs`: Additional field properties (label, required, options, etc.)

**Returns:**

-  `FieldOperationResponse`: Response containing field operation result

**Example:**

```python
response = client.add_field(
    app_id="APP123",
    requesting_user_email_address="user@example.com",
    section_index=0,
    field_index=1,
    field_type="singleLineText",
    label="Email",
    required=True
)
```

### `update_field(app_id, requesting_user_email_address, field_name, **kwargs)`

Updates an existing field in a Clappia app.

**Parameters:**

-  `app_id` (str): The app ID
-  `requesting_user_email_address` (str): Email of requesting user
-  `field_name` (str): Variable name of field to update
-  `**kwargs`: Field properties to update (label, required, options, etc.)

**Returns:**

-  `FieldOperationResponse`: Response containing field operation result

**Example:**

```python
response = client.update_field(
    app_id="APP123",
    requesting_user_email_address="user@example.com",
    field_name="email_field",
    label="Email Address",
    required=True
)
```

### `remove_page_break(app_id, requesting_user_email_address, page_index)`

Removes a page break from an app.

**Parameters:**

-  `app_id` (str): The app ID
-  `requesting_user_email_address` (str): Email of requesting user
-  `page_index` (int): Page index to remove (must be > 0)

**Returns:**

-  `PageBreakOperationResponse`: Response containing page break operation result

**Example:**

```python
response = client.remove_page_break(
    app_id="APP123",
    requesting_user_email_address="user@example.com",
    page_index=1
)
if response.success:
    print("Page break removed successfully")
```

### `add_page_break(app_id, requesting_user_email_address, page_index, section_index)`

Adds a page break to an app.

**Parameters:**

-  `app_id` (str): The app ID
-  `requesting_user_email_address` (str): Email of requesting user
-  `page_index` (int): Page index where to add page break
-  `section_index` (int): Section index where to add page break

**Returns:**

-  `PageBreakOperationResponse`: Response containing page break operation result

**Example:**

```python
response = client.add_page_break(
    app_id="APP123",
    requesting_user_email_address="user@example.com",
    page_index=1,
    section_index=0
)
if response.success:
    print(f"Page break added with ID: {response.page_id}")
```

### `update_page(app_id, requesting_user_email_address, page_index, page_id, **kwargs)`

Updates page break settings in an app.

**Parameters:**

-  `app_id` (str): The app ID
-  `requesting_user_email_address` (str): Email of requesting user
-  `page_index` (int): Page index to update
-  `page_id` (str): Page ID
-  `show_submit_button` (bool, optional): Show submit button
-  `previous_button_text` (str, optional): Previous button text
-  `next_button_text` (str, optional): Next button text

**Returns:**

-  `PageBreakOperationResponse`: Response containing page break operation result

**Example:**

```python
response = client.update_page(
    app_id="APP123",
    requesting_user_email_address="user@example.com",
    page_index=1,
    page_id="page_123",
    show_submit_button=True,
    previous_button_text="Go Back",
    next_button_text="Continue"
)
if response.success:
    print("Page settings updated successfully")
```

### `reorder_section(app_id, requesting_user_email_address, source_section_index, target_section_index, **kwargs)`

Reorders a section within an app.

**Parameters:**

-  `app_id` (str): The app ID
-  `requesting_user_email_address` (str): Email of requesting user
-  `source_section_index` (int): Source section index
-  `target_section_index` (int): Target section index
-  `source_page_index` (int, optional): Source page index
-  `target_page_index` (int, optional): Target page index

**Returns:**

-  `SectionOperationResponse`: Response containing section operation result

**Example:**

```python
response = client.reorder_section(
    app_id="APP123",
    requesting_user_email_address="user@example.com",
    source_section_index=0,
    target_section_index=2,
    source_page_index=0,
    target_page_index=1
)
if response.success:
    print("Section reordered successfully")
```

## Response Models

### `AppDefinitionResponse`

-  `success` (bool): Whether the operation was successful
-  `message` (str): Response message
-  `app_id` (str): App ID
-  `data` (dict): App definition data

### `AppCreationResponse`

-  `success` (bool): Whether the operation was successful
-  `message` (str): Response message
-  `app_id` (str): Generated app ID
-  `app_name` (str): Name of created app
-  `sections_created` (int): Number of sections created
-  `data` (dict): Additional response data

### `FieldOperationResponse`

-  `success` (bool): Whether the operation was successful
-  `message` (str): Response message
-  `app_id` (str): App ID where field was modified
-  `field_name` (str): Name of the field
-  `operation` (str): Type of operation performed
-  `data` (dict): Additional response data

### `PageBreakOperationResponse`

-  `success` (bool): Whether the operation was successful
-  `message` (str): Response message
-  `app_id` (str): App ID where page break was modified
-  `page_index` (int): Page index
-  `page_id` (str): Page ID
-  `operation` (str): Type of operation performed
-  `data` (dict): Additional response data

### `SectionOperationResponse`

-  `success` (bool): Whether the operation was successful
-  `message` (str): Response message
-  `app_id` (str): App ID where section was modified
-  `source_section_index` (int): Source section index
-  `target_section_index` (int): Target section index
-  `source_page_index` (int): Source page index
-  `target_page_index` (int): Target page index
-  `operation` (str): Type of operation performed
-  `data` (dict): Additional response data
