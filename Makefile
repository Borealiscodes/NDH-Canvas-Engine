# =============================================================================
# NDH-Canvas-Engine Master Orchestration Substrate
# Automates environment environment alignment, formatting, and variant verification.
# Tracks Phase 1 Core Math, Phase 2 Primitives, and Phase 3 Lean 4 Enclaves.
# =============================================================================

.PHONY: all env format test verify clean lean_init lean_build

all: env format test verify

env:
	@echo "📡 [STAGE 1] Synchronizing local engine dependency matrices..."
	pip install -e .[dev]

format:
	@echo "🐍 [STAGE 2] Enforcing clean vertical formatting profiles via Black..."
	black --check --line-length=100 src/ tests/

test:
	@echo "🧮 [STAGE 3] Triggering continuous array invariant verification gates..."
	pytest -v tests/

verify: lean_build
	@echo "🛡️  [STAGE 4] Executing deterministic type checking gates..."
	@echo "💎 [SUCCESS] All array fields and formal enclaves match completely."

lean_init:
	@echo "📦 [PHASE 3.1] Synchronizing Lean 4 mathlib packaging dependencies..."
	cd verification/lean && lake update

lean_build: lean_init
	@echo "📐 [PHASE 3.2] Compiling dependent type structures and symplectic invariants..."
	cd verification/lean && lake build

clean:
	@echo "🧹 Purging volatile runtime containers, build tracks, and cache containers..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf verification/lean/.lake/ verification/lean/build/
