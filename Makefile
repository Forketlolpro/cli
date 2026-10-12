.PHONY: lint test check types

VENV = .venv/bin


lint:
	$(VENV)/ruff check src/

test:
	$(VENV)/pytest

types:
	$(VENV)/pyrefly check src/

check: lint test types