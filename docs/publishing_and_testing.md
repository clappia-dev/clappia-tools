# Publishing, Testing, and Development Guide

This document explains how Clappia API Tools is published, how to run tests, and how to set up and test the module during development, including installing it in another repository.

---

## 1. Publishing (Automated via GitHub Actions)

Publishing to PyPI is automated using GitHub Actions. The workflow is defined in `.github/workflows/publish.yml` and is triggered on every push to the `master` branch or via manual dispatch.

**Key steps in the workflow:**
- Checks out the repository code
- Installs `uv` (a modern Python package/dependency manager)
- Sets up Python 3.10 using `uv`
- Builds the package with `uv build`
- Publishes the package to PyPI using `pypa/gh-action-pypi-publish`

**Manual publishing:**
- Push to the `master` branch, or
- Trigger the workflow manually from the GitHub Actions tab

---

## 2. Testing

Before running tests, ensure your `.env` file is present in the project root with valid credentials. The test suite will load environment variables automatically.

**Quick testing:**
```bash
pytest
```

**Run specific test types:**
```bash
pytest -m unit          # Unit tests only
pytest -m integration   # Integration tests only
pytest -m "not slow"    # Skip slow tests
```

**Testing with coverage:**
```bash
# First install test dependencies
uv pip install -e ".[test]"

# Then run with coverage
pytest --cov=clappia_api_tools --cov-report=html
```

**Using uv for isolated testing:**
```bash
# Run tests in isolated environment
uv run pytest

# Or with coverage
uv run pytest --cov=clappia_api_tools
```

---

## 3. Initial Setup Using uv

[uv](https://github.com/astral-sh/uv) is used for dependency management and building the package.

**Quick setup (recommended):**
```bash
uv venv
uv pip install -e ".[dev]"
```

**Traditional setup with activation:**
```bash
# Linux/macOS
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"

# Windows
uv venv
.venv\Scripts\activate
uv pip install -e ".[dev]"
```

This will create a virtual environment and install all development dependencies in editable mode.

---

## 4. Testing the Module in Another Repository (Development Workflow)

To test changes to Clappia API Tools in another project before publishing:

### Method 1: Local Wheel Installation

1. **Build a local wheel:**
   ```bash
   uv build
   # Creates: dist/clappia_api_tools-1.0.0-py3-none-any.whl
   ```

2. **Install the wheel in your other project:**
   ```bash
   # In your other project's virtual environment
   pip install /path/to/clappia-api-tools/dist/clappia_api_tools-1.0.0-py3-none-any.whl
   
   # Or copy the wheel file to your project directory
   pip install ./clappia_api_tools-1.0.0-py3-none-any.whl
   ```

### Method 2: Editable Installation (Recommended for Development)

```bash
# In your other project's virtual environment
pip install -e /absolute/path/to/clappia-api-tools
```

This allows you to test your changes in real-time without rebuilding.

### Method 3: Direct Git Installation

```bash
# Install from local git repo
pip install git+file:///absolute/path/to/clappia-api-tools

# Or from a specific branch
pip install git+file:///absolute/path/to/clappia-api-tools@your-branch
```

---

## 5. Development Workflow

**Typical development cycle:**

1. **Make changes** to the codebase
2. **Run tests** to ensure nothing breaks:
   ```bash
   pytest -v
   ```
3. **Format code** with Black:
   ```bash
   black clappia_api_tools/
   ```
4. **Type check** with mypy:
   ```bash
   mypy clappia_api_tools/
   ```
5. **Test in another project** using Method 2 above
6. **Commit and push** to trigger publishing

**All-in-one development check:**
```bash
black clappia_api_tools/ && mypy clappia_api_tools/ && pytest -v
```

---

For more details, see the [publish.yml workflow](../.github/workflows/publish.yml) and the main [README.md](../README.md).