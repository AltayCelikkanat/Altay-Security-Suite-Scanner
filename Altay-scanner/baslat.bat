@echo off
title Altay Security Suite - Baslatici
echo ===========================================
echo   Altay Security Suite - Kurulum ve Baslatma
echo ===========================================

:: Python yuklu mu kontrol et
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [HATA] Python sistemde bulunamadi!
    echo Lutfen python.org adresinden Python kurun.
    pause
    exit /b
)

echo [1/2] Gerekli kutuphaneler yukleniyor...
pip install -r requirements.txt --quiet

echo [2/2] Altay Scanner baslatiliyor...
python main.py

echo.
echo Program kapatildi.
pause