# ridhun

Starter Python project: a small package with a CLI, tests, linting, and CI.

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```sh
uv sync
```

## Usage

```sh
uv run ridhun            # Hello, world!
uv run ridhun Ridhun     # Hello, Ridhun!
```

## Development

```sh
uv run pytest            # tests
uv run ruff check .      # lint
uv run ruff format .     # format
```

## Layout

```
src/ridhun/   package code (core.py, cli.py)
tests/        pytest tests
```
