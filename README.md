# daily-bible-share

## Development

Install dependencies:

```bash
uv sync
```

Run the FastAPI development server:

```bash
uv run uvicorn app.main:app --reload
```

Quick manual health check:

```bash
curl http://127.0.0.1:8000/health
```

Expected response shape:

```json
{
  "status": "ok",
  "service": "daily-bible-share",
  "version": "0.1.0"
}
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

## Commit Message Template

This repository provides `.gitmessage` with the same title format as PR title lint:

`<type>(<scope>): <subject>`

Set it once in this repo:

```bash
git config commit.template .gitmessage
```

Then `git commit` will open with the format guidance.
