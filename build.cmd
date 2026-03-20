@echo off
TITLE "NATO Enclave CMDB Manager - Build & Launch"
echo ======================================================================
echo NATO Enclave CMDB Manager ^| CONFIANZA23 Inteligencia y Seguridad, S.L.
echo ======================================================================
echo.

echo [1/3] Checking Python environment...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH.
    pause
    exit /b %errorlevel%
)

echo [2/3] Installing/Updating dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install dependencies.
    pause
    exit /b %errorlevel%
)

echo [3/3] Launching Streamlit Application...
echo.
echo The application will be available at http://localhost:8501
echo.
streamlit run app.py

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Application crashed or was interrupted.
    pause
)

echo.
echo Build script finished.
pause
