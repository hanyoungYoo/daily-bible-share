# daily-bible-share

## Development

Install development dependencies:

```bash
uv sync
```

Run lint checks:

```bash
uv run ruff check .
uv run ruff format --check .
```

Auto-fix and format:

```bash
uv run ruff check . --fix
uv run ruff format .
```
