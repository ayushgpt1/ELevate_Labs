@echo off
echo ==========================================
echo  🚀 Face Mask Detection Setup - Windows
echo ==========================================
echo.

REM Step 1: Navigate into scripts folder
cd scripts

REM Step 2: Create virtual environment (in root folder)
cd ..
python -m venv myvenv
if errorlevel 1 (
    echo ❌ Failed to create virtual environment.
    pause
    exit /b
)

REM Step 3: Activate the virtual environment
call myvenv\Scripts\activate

REM Step 4: Upgrade pip
echo 🔄 Upgrading pip...
python -m pip install --upgrade pip

REM Step 5: Install required packages
echo 📦 Installing Python packages...
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Failed to install dependencies.
    pause
    exit /b
)
REM Step 6: Train the model 
echo train the model 
python scripts\train.py 
if errorlevel 1 (
    echo ❌ Failed 
    pause
    exit /b
)
REM Step 7: Run the GUI app
echo ✅ Launching Face Mask Detection GUI...
python scripts\app.py

pause
