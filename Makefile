.PHONY: install install-dev install-hooks format lint check clean build lock sync

# Installation
install: ## Install the package in production mode
	uv pip install -e .

install-dev: ## Install the package with development dependencies
	uv sync --all-extras

# Code Formatting & Linting
format: ## Format code with ruff
	uv run ruff format .
	uv run ruff check . --fix

lint: ## Run linting and type checking
	uv run ruff check .
	uv run mypy .

check: format lint ## Run all checks

# Cleanup
clean: ## Clean up build artifacts and cache
	rm -rf build/ dist/ *.egg-info/ .mypy_cache/ .ruff_cache/
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

# Build
build: clean ## Build the package
	uv build

# Lock Management
lock: ## Generate/update lock file
	uv lock

sync: ## Sync environment with lock file
	uv sync
