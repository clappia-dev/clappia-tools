# Clappia API Tools

**Clappia APIs SDK**

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/clappia-tools)](https://pypi.org/project/clappia-tools/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Overview

Clappia API Tools is a Python package that provides a set of clients for seamless integration with the [Clappia API](https://developer.clappia.com/). It enables developers to automate workflows, manage submissions, and interact with Clappia apps programmatically. The package is designed for use in automation, data integration, and agent-based systems (e.g., LangChain agents, MCP).

---

## Features

-  **Multiple API Clients**: Dedicated clients for each Clappia API operation.
-  **Submission Management**: Create, edit, update owners, and change status of submissions.
-  **App Definition Retrieval**: Fetch complete app structure and metadata.
-  **App Management**: Manage the app structure via fields and sections updates.
-  **Input Validation**: Built-in validation for IDs, emails, and status objects.
-  **Comprehensive Testing**: Includes unit and integration tests.

---

## Available Clients

-  `SubmissionClient`: Manage submissions (create, edit, update owners, change status)
-  `AppDefinitionClient`: Retrieve app definitions and metadata
-  `AppManagementClient`: Manage app structure (fields, sections, creation)

---

## Documentation

-  [Submission Client Reference](docs/submission_client.md)
-  [App Definition Client Reference](docs/app_definition_client.md)
-  [App Management Client Reference](docs/app_management_client.md)
-  [Tool Functions Reference](docs/tools.md)
-  [Advanced Usage](docs/advanced_usage.md)

---

## Installation

```bash
pip install clappia-api-tools
```

Or, for development:

```bash
git clone https://github.com/clappia-dev/clappia-api-tools.git
cd clappia-api-tools
pip install -e .[dev]
```

---

## First-Time Setup

Before using or testing Clappia API Tools, set up your environment variables. Create a `.env` file in the project root with the following content:

```env
CLAPPIA_API_KEY=your-api-key
CLAPPIA_BASE_URL=https://api.clappia.com
CLAPPIA_WORKPLACE_ID=your-workplace-id
```

-  Replace `your-api-key` and `your-workplace-id` with your actual Clappia credentials.
-  The `.env` file is included in `.gitignore` and will not be committed.
-  The package uses [python-dotenv](https://pypi.org/project/python-dotenv/) to load these variables automatically if present.

---

## Configuration

You must provide your Clappia API credentials and workspace information directly when initializing any client:

-  `api_key`: Your Clappia API key
-  `base_url`: The base URL for the Clappia API (e.g., `https://api.clappia.com`)
-  `workplace_id`: Your Clappia workplace ID

---

## Usage

### SubmissionClient Example

```python
from clappia_api_tools.client.submission_client import SubmissionClient

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
```

### AppDefinitionClient Example

```python
from clappia_api_tools.client.app_definition_client import AppDefinitionClient

client = AppDefinitionClient(
    api_key="your-api-key",
    base_url="https://api.clappia.com",
    workplace_id="your-workplace-id"
)

# Get app definition
result = client.get_definition(app_id="MFX093412")
print(result)
```

### AppManagementClient Example

```python
from clappia_api_tools.client.app_management_client import AppManagementClient

client = AppManagementClient(
    api_key="your-api-key",
    base_url="https://api.clappia.com",
    workplace_id="your-workplace-id"
)

# Example: create a new app
# result = client.create_app(app_name="My New App", requesting_user_email_address="user@example.com", sections=[...])
# print(result)
```

---

## Input Validation

-  **App ID**: Must be uppercase letters and numbers (e.g., `MFX093412`).
-  **Submission ID**: Must be uppercase letters and numbers (e.g., `HGO51464561`).
-  **Email**: Must be a valid email address.
-  **Status**: Must be a dictionary with a non-empty `statusName` or `name` field.

Invalid inputs will return descriptive error messages.

---

## Testing

Before running tests, ensure your `.env` file is present in the project root with valid credentials. The test suite will load environment variables automatically.

Run all tests (unit and integration):

```bash
pytest
```

---

## Contributing

1. Fork the repository and create your branch.
2. Write clear, well-documented code and tests.
3. Run `pytest` and ensure all tests pass.
4. Submit a pull request with a clear description of your changes.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
