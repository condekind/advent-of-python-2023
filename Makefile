

all:
	poetry run mypy --check-untyped-defs advent2023/
	poetry run ruff check advent2023/
	poetry run ruff format advent2023/
	poetry run clean
	@rm -rf ./util/__pycache__

.PHONY: fmt lint check

# check is just an alias for lint
check: lint

lint:
	poetry run mypy --check-untyped-defs advent2023/
	poetry run ruff check advent2023/

fmt:
	poetry run ruff format advent2023/

clean:
	poetry run clean
	@rm -rf ./util/__pycache__

