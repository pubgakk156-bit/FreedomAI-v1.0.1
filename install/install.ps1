Clear-Host

Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "      FreedomAI v1.0.1 Installer" -ForegroundColor Green
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

# -----------------------
# FOLDERS
# -----------------------

$folders = @(
    "app",
    "app/database",
    "app/handlers",
    "app/handlers/finance",
    "app/keyboards",
    "app/repositories",
    "app/services",
    "app/states",
    "app/utils",

    "data",
    "docs",
    "install",
    "tests",

    "tools",

    ".github"
)

foreach($folder in $folders){

    if(!(Test-Path $folder)){
        New-Item -ItemType Directory -Path $folder | Out-Null
        Write-Host "[DIR ] $folder" -ForegroundColor Green
    }
}

# -----------------------
# FILES
# -----------------------

$files = @(

    "main.py",
    "requirements.txt",
    "README.md",
    "CHANGELOG.md",
    "ROADMAP.md",
    "VERSION",
    ".gitignore",

    "app/__init__.py",
    "app/config.py",

    "app/database/__init__.py",
    "app/database/database.py",

    "app/handlers/__init__.py",
    "app/handlers/start.py",

    "app/handlers/finance/__init__.py",
    "app/handlers/finance/menu.py",
    "app/handlers/finance/income.py",
    "app/handlers/finance/expense.py",
    "app/handlers/finance/balance.py",
    "app/handlers/finance/history.py",
    "app/handlers/finance/delete_transaction.py",
    "app/handlers/finance/edit_transaction.py",

    "app/keyboards/__init__.py",
    "app/keyboards/main_keyboard.py",
    "app/keyboards/finance_keyboard.py",
    "app/keyboards/category_keyboard.py",
    "app/keyboards/history_keyboard.py",

    "app/repositories/__init__.py",
    "app/repositories/user_repository.py",
    "app/repositories/finance_repository.py",
    "app/repositories/category_repository.py",

    "app/services/__init__.py",
    "app/services/user_service.py",
    "app/services/finance_service.py",
    "app/services/navigation_service.py",

    "app/states/__init__.py",
    "app/states/finance_states.py",

    "tools/run.py",
    "tools/project_info.py",
    "tools/system_check.py",
    "tools/db_viewer.py",
    "tools/db_reset.py",
    "tools/db_backup.py",
    "tools/git_tool.py"
)

foreach($file in $files){

    if(!(Test-Path $file)){
        New-Item -ItemType File -Path $file | Out-Null
        Write-Host "[FILE] $file" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host " Project structure successfully created!" -ForegroundColor Green
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""