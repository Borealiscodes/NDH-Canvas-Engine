# =============================================================================
# NDH-Canvas-Engine Orchestration Substrate
# Automates environment environment alignment, formatting, and variant verification.
# =============================================================================

.PHONY: all env format test clean

all: env format test

env:
	@echo "📡 [CANVAS] Synchronizing local engine dependency matrices..."
	pip install -e .[dev]

format:
	@echo "🐍 [CANVAS] Enforcing clean vertical formatting profiles via Black..."
	black --check --line-length=100 src/ tests/

test:
	@echo "🧮 [CANVAS] Triggering continuous array invariant verification gates..."
	pytest -v tests/

clean:
	@echo "🧹 Purging volatile runtime containers and local module cache tracks..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
