# ==========================================
#   🛠 Clappia API Tools - Development Makefile
# ==========================================

.PHONY: help install install-dev format lint check clean pre-commit-run security

# ------------------------------------------
# 🌟 Colors
# ------------------------------------------
CYAN=\033[36m
GREEN=\033[32m
YELLOW=\033[33m
RED=\033[31m
RESET=\033[0m

# ------------------------------------------
# 💡 Default target
# ------------------------------------------
help: ## Show this awesome help message
	@echo ""
	@echo "$(CYAN)==========================================$(RESET)"
	@echo "$(CYAN)     🛠 Clappia API Tools - Makefile$(RESET)"
	@echo "$(CYAN)==========================================$(RESET)"
	@echo ""
	@echo "Available commands:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| sort \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-20s$(RESET) %s\n", $$1, $$2}'
	@echo ""

# ==========================================
# ⚡ Installation
# ==========================================
install: ## Install the package in production mode
	@echo "$(YELLOW)Installing package...$(RESET)"
	uv pip install -e .

install-dev: ## Install the package with development dependencies
	@echo "$(YELLOW)Installing development dependencies...$(RESET)"
	uv sync --all-extras

# ==========================================
# 🎨 Code Formatting & Linting
# ==========================================
format: ## Format code with ruff
	@echo "$(YELLOW)Running ruff formatter...$(RESET)"
	uv run ruff format .
	@echo "$(YELLOW)Applying ruff fixes...$(RESET)"
	uv run ruff check . --fix
	@echo "$(GREEN)Code formatting complete!$(RESET)"

lint: ## Run linting and type checking
	@echo "$(YELLOW)Running ruff linting...$(RESET)"
	uv run ruff check .
	@echo "$(YELLOW)Running mypy type checking...$(RESET)"
	uv run mypy .
	@echo "$(GREEN)Linting complete!$(RESET)"

# ==========================================
# 🔒 Security & Quality
# ==========================================
security: ## Run security checks
	@echo "$(YELLOW)Running security checks...$(RESET)"
	uv run bandit -r clappia_api_tools/
	uv run safety check

audit: ## Run dependency audit
	@echo "$(YELLOW)Running dependency audit...$(RESET)"
	uv run pip-audit

# ==========================================
# ✅ All Checks
# ==========================================
check: format lint security ## Run all checks
	@echo "$(GREEN)All checks completed!$(RESET)"

quick-check: ## Quick check (linting and formatting only)
	@echo "$(YELLOW)Running quick checks...$(RESET)"
	uv run ruff check .
	uv run ruff format --check .
	uv run mypy .

# ==========================================
# 🧹 Pre-commit (for local testing only - CI runs automatically)
# ==========================================
pre-commit-run: ## Run pre-commit on all files (CI runs this automatically)
	@echo "$(YELLOW)Running pre-commit on all files...$(RESET)"
	uv run pre-commit run --all-files

pre-commit-update: ## Update pre-commit hooks
	@echo "$(YELLOW)Updating pre-commit hooks...$(RESET)"
	uv run pre-commit autoupdate

# ==========================================
# 🧹 Cleanup
# ==========================================
clean: ## Clean up build artifacts and cache
	@echo "$(YELLOW)Cleaning up...$(RESET)"
	rm -rf build/ dist/ *.egg-info/ .mypy_cache/ .ruff_cache/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	@echo "$(GREEN)Cleanup complete!$(RESET)"

# ==========================================
# 🚀 Development Workflow
# ==========================================
dev-setup: install-dev ## Complete development setup
	@echo "$(GREEN)Development setup complete!$(RESET)"
	@echo "You can now run 'make check' to verify everything works."
	@echo "$(YELLOW)Note: Pre-commit checks run automatically on GitHub via CI.$(RESET)"

# ==========================================
# 📚 Documentation
# ==========================================
docs-serve: ## Serve documentation locally
	@echo "$(YELLOW)Serving documentation...$(RESET)"
	uv run mkdocs serve

docs-build: ## Build documentation
	@echo "$(YELLOW)Building documentation...$(RESET)"
	uv run mkdocs build

# ==========================================
# 🏗 Release
# ==========================================
build: clean ## Build the package
	@echo "$(YELLOW)Building package...$(RESET)"
	uv build

build-check: build ## Build and check the package
	@echo "$(YELLOW)Checking built package...$(RESET)"
	uv run twine check dist/*

# ==========================================
# 🔢 Version Management
# ==========================================
version: ## Show current version
	@python -c "import re; content = open('pyproject.toml').read(); match = re.search(r'version = \"([^\"]+)\"', content); print(match.group(1) if match else 'Version not found')"

# ==========================================
# 🔒 Lock Management
# ==========================================
lock: ## Generate/update lock file
	uv lock

sync: ## Sync environment with lock file  
	uv sync

# ==========================================
# 📂 Utilities
# ==========================================
tree: ## Show project structure (requires tree command: brew install tree / apt-get install tree)
	@echo "$(YELLOW)Project structure:$(RESET)"
	@which tree > /dev/null 2>&1 && tree -I '__pycache__|*.pyc|.git|.venv|build|dist|*.egg-info' -a || echo "$(RED)Error: 'tree' command not found. Install it with: brew install tree (macOS) or apt-get install tree (Linux)$(RESET)"

dependencies: ## Show dependency tree
	@echo "$(YELLOW)Dependency tree:$(RESET)"
	uv tree
