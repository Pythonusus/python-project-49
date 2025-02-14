install:
	uv sync

brain-games:
	uv run brain-games

lint:
	uv run ruff check brain_games

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install --force dist/*.whl

.PHONY: install brain-games lint build publish package-install package-reinstall
