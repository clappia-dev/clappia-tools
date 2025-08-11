# Setup, Testing, and Publishing Guide

A comprehensive guide for setting up, testing, and publishing the Clappia API Tools package.

---

## 📋 Table of Contents

1. [Repository Setup](#1-repository-setup)
2. [Environment Setup](#2-environment-setup)
3. [Development Setup](#3-development-setup)
4. [Testing Guide](#4-testing-guide)
5. [Publishing Workflow](#5-publishing-workflow)

---

## 1. Repository Setup

### Clone the Repository

```bash
# Clone the repository
git clone https://github.com/clappia-dev/clappia-api-tools.git

# Navigate to the project directory
cd clappia-api-tools
```

---

## 2. Environment Setup

### Prerequisites

-  Python 3.10 or higher
-  [uv](https://github.com/astral-sh/uv) package manager
-  Git

### Install uv

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Verify installation
uv --version
```

---

## 3. Development Setup

### Create Virtual Environment

```bash
# Create virtual environment using uv
uv venv

# Activate virtual environment
# macOS/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### Install Dependencies

```bash
# Install all dependencies (including dev and test)
uv sync --extra dev --extra test

# Or install separately
uv sync                    # Core dependencies
uv sync --extra dev        # Development dependencies
uv sync --extra test       # Test dependencies
```

---

## 4. Testing Guide

### Basic Testing

```bash
# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run specific test types
uv run pytest clappia_api_tools/tests/unit/          # Unit tests only
uv run pytest clappia_api_tools/tests/integration/   # Integration tests only
```

### Individual File Testing

```bash
# Test a specific test file
uv run pytest clappia_api_tools/tests/unit/client/test_client.py

# Test a specific test class
uv run pytest clappia_api_tools/tests/unit/client/test_client.py::TestSubmissionClient

# Test a specific test method
uv run pytest clappia_api_tools/tests/unit/client/test_client.py::TestSubmissionClient::test_create_submission_success

# Test by directory
uv run pytest clappia_api_tools/tests/unit/client/
uv run pytest clappia_api_tools/tests/integration/submission/
```

### Testing with Coverage

```bash
# Run with coverage
uv run pytest --cov=clappia_api_tools --cov-report=term-missing

# Generate HTML coverage report
uv run pytest --cov=clappia_api_tools --cov-report=html
```

### Advanced Testing Options

```bash
# Test and stop on first failure
uv run pytest -x

# Test with print statements visible
uv run pytest -s

# Test with maximum verbosity
uv run pytest -vvv
```

---

## 5. Publishing Workflow

Publishing to PyPI is automated using GitHub Actions. The workflow is defined in `.github/workflows/publish.yml`.

### Workflow Steps

1. **Checkout** - Retrieves the repository code
2. **Install uv** - Sets up the modern Python package manager
3. **Set up Python 3.10** - Installs Python using `uv python install 3.10`
4. **Build package** - Creates distribution files with `uv build`
5. **Publish to PyPI** - Uploads to PyPI using `pypa/gh-action-pypi-publish`

---

## Quick Reference

| Command                                              | Description                      |
| ---------------------------------------------------- | -------------------------------- |
| `uv venv`                                            | Create virtual environment       |
| `uv sync`                                            | Install dependencies             |
| `uv sync --extra dev`                                | Install development dependencies |
| `uv sync --extra test`                               | Install test dependencies        |
| `uv run pytest`                                      | Run all tests                    |
| `uv run pytest -v`                                   | Run tests with verbose output    |
| `uv run pytest clappia_api_tools/tests/unit/`        | Run only unit tests              |
| `uv run pytest clappia_api_tools/tests/integration/` | Run only integration tests       |
| `uv run pytest --cov=clappia_api_tools`              | Run tests with coverage          |
| `uv lock`                                            | Update lock file                 |

---

## Additional Resources

-  [Main README.md](../README.md)
-  [uv Documentation](https://github.com/astral-sh/uv)
-  [pytest Documentation](https://docs.pytest.org/)
