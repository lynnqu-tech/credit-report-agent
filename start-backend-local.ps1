$env:SECRET_KEY = "local-development-secret"
$env:ADMIN_USERNAME = "analyst"
$env:ADMIN_PASSWORD = "123456"
$env:DATABASE_URL = "sqlite:///./credit_agent.db"
$env:REDIS_URL = "redis://127.0.0.1:6379/0"
$env:QWEN_API_KEY = ""

Set-Location (Join-Path $PSScriptRoot "credit_report_agent\.worktrees\feat-mvp\backend")
& ".\.venv\Scripts\python.exe" -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
