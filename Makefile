

all:
	source .venv/bin/activate && poetry run mypy --check-untyped-defs advent2023/
	source .venv/bin/activate && poetry run ruff check advent2023/
	source .venv/bin/activate && poetry run ruff format advent2023/
	source .venv/bin/activate && poetry run clean
	@rm -rf ./util/__pycache__

.PHONY: fmt lint check

# check is just an alias for lint
check: lint

lint:
	source .venv/bin/activate && poetry run mypy --check-untyped-defs advent2023/
	source .venv/bin/activate && poetry run ruff check advent2023/

fmt:
	source .venv/bin/activate && poetry run ruff format advent2023/

clean:
	source .venv/bin/activate && poetry run clean
	@rm -rf ./util/__pycache__

