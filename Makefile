# Makefile
install:
	uv sync

lint:
	uv run ruff check src

brain-games:
	uv run brain-games