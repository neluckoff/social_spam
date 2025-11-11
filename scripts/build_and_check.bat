@echo off
REM Script to build and verify the package locally before publishing (Windows)

echo ================================
echo Building social_spam package...
echo ================================
echo.

REM Clean previous builds
echo Cleaning previous builds...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist *.egg-info rmdir /s /q *.egg-info
echo.

REM Install build tools
echo Installing build tools...
python -m pip install --upgrade pip build twine check-wheel-contents --quiet
echo.

REM Build the package
echo Building package...
python -m build
echo.

REM Check build files
echo Built files:
dir dist
echo.

REM Verify package integrity
echo Checking package integrity...
twine check dist/*
echo.

REM Check wheel contents
echo Checking wheel contents...
check-wheel-contents dist/*.whl
echo.

REM Test installation in virtual environment
echo Testing installation...
python -m venv test_venv
call test_venv\Scripts\activate.bat

pip install --quiet dist\*.whl
echo.

REM Test imports
echo Testing imports...
python -c "from social_spam import Mail, Telegram, Vkontakte, WhatsApp; print('All imports successful!')"
echo.

REM Cleanup
call deactivate
rmdir /s /q test_venv

echo.
echo ✅ Build verification complete!
echo.
echo Package files:
dir dist
echo.
echo Ready to publish!
echo.
echo To publish to PyPI:
echo   twine upload dist/*
echo.
pause

