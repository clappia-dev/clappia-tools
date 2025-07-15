# App Definition Client Reference

This document provides a detailed reference for the `AppDefinitionClient` in the Clappia API Tools package.

## Overview

The `AppDefinitionClient` handles operations related to retrieving app definitions and metadata from Clappia.

## Import

```python
from clappia_api_tools.client.app_definition_client import AppDefinitionClient
```

## Initialization

Instantiate `AppDefinitionClient` directly with the required parameters:

```python
client = AppDefinitionClient(
    api_key="your-api-key",
    base_url="https://api.clappia.com",
    workplace_id="your-workplace-id"
)
```

## Methods

### get_definition

```python
def get_definition(app_id: str, language: str = "en", strip_html: bool = True, include_tags: bool = True) -> str
```

Fetches complete definition of a Clappia application including forms, fields, sections, and metadata.

**Args:**

-  `app_id` (str): Unique application identifier in uppercase letters and numbers format (e.g., QGU236634).
-  `language` (str, optional): Language code for field labels and translations. Default is "en". Options: "en", "es", "fr", "de".
-  `strip_html` (bool, optional): Whether to remove HTML formatting from text fields. Default is True.
-  `include_tags` (bool, optional): Whether to include metadata tags in response. Default is True.

**Returns:**

-  `str`: Formatted response with app definition details and complete structure.

## Usage Example

```python
from clappia_api_tools.client.app_definition_client import AppDefinitionClient

client = AppDefinitionClient(
    api_key="your-api-key",
    base_url="https://api.clappia.com",
    workplace_id="your-workplace-id"
)

result = client.get_definition(app_id="MFX093412")
print(result)
```
