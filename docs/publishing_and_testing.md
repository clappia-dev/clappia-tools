# Publishing, Testing, and Development Guide

This document explains how Clappia API Tools is published, how to run tests, and how to set up and test the module during development, including installing it in another repository.

---

## 1. Publishing (Automated via GitHub Actions)

Publishing to PyPI is automated using GitHub Actions. The workflow is defined in `.github/workflows/publish.yml` and is triggered on every push to the `master` branch or via manual dispatch.

**Key steps in the workflow:**

-  Checks out the repository code
-  Installs `uv` (a modern Python package/dependency manager)
-  Sets up Python 3.10 using `uv`
-  Builds the package with `uv build`
-  Publishes the package to PyPI using `pypa/gh-action-pypi-publish`

**Manual publishing:**

-  Push to the `master` branch, or
-  Trigger the workflow manually from the GitHub Actions tab

---

## 2. Testing

Before running tests, ensure your `.env` file is present in the project root with valid credentials. The test suite will load environment variables automatically.

**To run all tests (unit and integration):**

```bash
pytest
```

You can also use `uv` to run tests in a clean environment:

```bash
uv venv
source .venv/bin/activate
uv pip install -e .[dev]
pytest
```

---

## 3. Initial Setup Using uv

[uv](https://github.com/astral-sh/uv) is used for dependency management and building the package.

**To set up the project for development:**

```bash
uv venv
source .venv/bin/activate
uv pip install -e .[dev]
```

This will create a virtual environment, activate it, and install all development dependencies in editable mode.

---

## 4. Testing the Module in Another Repository (Development Workflow)

To test changes to Clappia API Tools in another project before publishing:

1. **Build a local wheel:**

   ```bash
   uv build
   # The wheel file will be in the dist/ directory
   ```

2. **Install the wheel in your other project:**

   -  Copy the `.whl` file from `dist/` to your other project's directory
   -  In the other project's virtual environment, run:
      ```bash
      pip install ./clappia_api_tools-<version>-py3-none-any.whl
      ```
   -  Or, for editable installs (if both repos are local):
      ```bash
      pip install -e /path/to/clappia-api-tools
      ```

3. **Alternatively, install directly from a local path:**
   ```bash
   pip install -e /absolute/path/to/clappia-api-tools
   ```

This allows you to test your changes in a real project before publishing to PyPI.

---

For more details, see the [publish.yml workflow](../.github/workflows/publish.yml) and the main [README.md](../README.md).
