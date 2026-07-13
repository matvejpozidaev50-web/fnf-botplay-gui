#!/usr/bin/env python3
"""
Скрипт для создания EXE файла из проекта FNF BotPlay GUI
Использует PyInstaller для создания standalone исполняемого файла
"""

import subprocess
import sys
from pathlib import Path


def build_exe():
    """
Создает EXE файл из проекта
    """
    print("="*60)
    print("FNF BotPlay GUI - EXE Builder")
    print("="*60)
    
    # Проверяем наличие PyInstaller
    try:
        import PyInstaller
    except ImportError:
        print("\n[!] PyInstaller не установлен!")
        print("Установите: pip install pyinstaller")
        sys.exit(1)
    
    print("\n[*] Начинаем сборку EXE файла...\n")
    
    # Команда для PyInstaller
    command = [
        "pyinstaller",
        "--name=FNF_BotPlay_GUI",
        "--onefile",
        "--windowed",
        "--icon=assets/icon.ico",
        "--add-data=config.json:.",
        "--hidden-import=PyQt5",
        "--hidden-import=loguru",
        "--hidden-import=pydantic",
        "--hidden-import=PIL",
        "--hidden-import=cv2",
        "--hidden-import=numpy",
        "--hidden-import=pynput",
        "--collect-all=PyQt5",
        "--noupx",
        "--distpath=dist",
        "--buildpath=build",
        "--specpath=spec",
        "main.py",
    ]
    
    try:
        result = subprocess.run(command, check=True)
        print("\n" + "="*60)
        print("[✓] EXE файл успешно создан!")
        print("[✓] Файл находится в: dist/FNF_BotPlay_GUI.exe")
        print("="*60)
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n[!] Ошибка при сборке EXE: {e}")
        return False


if __name__ == "__main__":
    success = build_exe()
    sys.exit(0 if success else 1)
