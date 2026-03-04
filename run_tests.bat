@echo off

REM Activate virtual environment
call .venv\Scripts\activate

REM Run test suite
python -m pytest -v --webdriver Chrome --headless

REM Capture exit code
IF %ERRORLEVEL% EQU 0 (
    echo All tests passed ✅
    exit /b 0
) ELSE (
    echo Tests failed ❌
    exit /b 1
)