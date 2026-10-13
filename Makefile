.PHONY: format lint test check types

VENV = .venv/bin

format:
	$(VENV)/ruff format currency_rates/
	$(VENV)/ruff check --fix currency_rates/

lint:
	$(VENV)/ruff check currency_rates/

test:
	$(VENV)/pytest

types:
	$(VENV)/pyrefly check currency_rates/

check: lint test types