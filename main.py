#!/usr/bin/env python3
"""
FNF BotPlay GUI - Main Application
"""

import sys
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtCore import Qt
except ImportError:
    print("PyQt5 не установлен. Установите: pip install PyQt5")
    sys.exit(1)

from gui.main_window import MainWindow
from utils.config import Config

def main():
    """Main application entry point"""
    # Load config
    config = Config()
    
    # Create Qt application
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    # Create and show main window
    window = MainWindow(config)
    window.show()
    
    print("[*] FNF BotPlay GUI запущен")
    print("[*] F1 - Запуск | F2 - Стоп | ESC - Выход")
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
