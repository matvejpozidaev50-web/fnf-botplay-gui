#!/usr/bin/env python3
"""
Генератор GUI компонентов
"""

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTabWidget, QPushButton, QComboBox, QSpinBox,
    QLabel, QLineEdit, QCheckBox, QProgressBar,
    QTextEdit, QFileDialog, QMessageBox, QSlider
)
from PyQt5.QtCore import Qt, pyqtSignal, QThread
from PyQt5.QtGui import QIcon, QFont


class MainWindow(QMainWindow):
    """
Главное окно приложения
    """
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """
Инициализация интерфейса
        """
        self.setWindowTitle("FNF BotPlay GUI")
        self.setGeometry(100, 100, 1200, 800)
        
        # Создание главного виджета
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Главный layout
        main_layout = QHBoxLayout()
        
        # Боковая панель
        left_panel = self.create_left_panel()
        main_layout.addWidget(left_panel, 1)
        
        # Основное содержимое
        right_panel = self.create_right_panel()
        main_layout.addWidget(right_panel, 2)
        
        central_widget.setLayout(main_layout)
    
    def create_left_panel(self):
        """
Создание левой панели
        """
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Заголовок
        title = QLabel("УПРАВЛЕНИЕ")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        layout.addWidget(title)
        
        layout.addSpacing(20)
        
        # Выбор двигателя
        layout.addWidget(QLabel("Двигатель:"))
        self.engine_combo = QComboBox()
        self.engine_combo.addItems(["Psych Engine", "Kade Engine", "v-slice", "Базовый FNF"])
        layout.addWidget(self.engine_combo)
        
        layout.addSpacing(10)
        
        # Выбор песни
        layout.addWidget(QLabel("Песня:"))
        self.song_combo = QComboBox()
        self.song_combo.addItems(["Bopeebo", "Fresh", "Dadbattle", "Philly Nice"])
        layout.addWidget(self.song_combo)
        
        layout.addSpacing(10)
        
        # Выбор сложности
        layout.addWidget(QLabel("Сложность:"))
        self.difficulty_combo = QComboBox()
        self.difficulty_combo.addItems(["Easy", "Normal", "Hard", "Nightmare"])
        layout.addWidget(self.difficulty_combo)
        
        layout.addSpacing(10)
        
        # Кнопки управления
        self.start_btn = QPushButton("▶ ЗАПУСТИТЬ")
        self.start_btn.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold; padding: 10px;")
        layout.addWidget(self.start_btn)
        
        self.stop_btn = QPushButton("⏹ ОСТАНОВИТЬ")
        self.stop_btn.setStyleSheet("background-color: #f44336; color: white; font-weight: bold; padding: 10px;")
        layout.addWidget(self.stop_btn)
        
        layout.addSpacing(20)
        
        # Чекбоксы опций
        self.record_replay_cb = QCheckBox("Записывать реплеи")
        self.record_replay_cb.setChecked(True)
        layout.addWidget(self.record_replay_cb)
        
        self.auto_retry_cb = QCheckBox("Автоматический повтор")
        self.auto_retry_cb.setChecked(True)
        layout.addWidget(self.auto_retry_cb)
        
        layout.addSpacing(20)
        
        # Ползунок точности
        layout.addWidget(QLabel("Порог точности (%):"))
        self.accuracy_slider = QSlider(Qt.Horizontal)
        self.accuracy_slider.setMinimum(50)
        self.accuracy_slider.setMaximum(100)
        self.accuracy_slider.setValue(80)
        layout.addWidget(self.accuracy_slider)
        
        self.accuracy_label = QLabel("80%")
        layout.addWidget(self.accuracy_label)
        
        layout.addStretch()
        
        widget.setLayout(layout)
        return widget
    
    def create_right_panel(self):
        """
Создание правой панели
        """
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Табы
        tabs = QTabWidget()
        
        # Таб 1: Статистика
        stats_widget = self.create_stats_tab()
        tabs.addTab(stats_widget, "📊 Статистика")
        
        # Таб 2: Логи
        logs_widget = self.create_logs_tab()
        tabs.addTab(logs_widget, "📝 Логи")
        
        # Таб 3: Настройки
        settings_widget = self.create_settings_tab()
        tabs.addTab(settings_widget, "⚙️ Настройки")
        
        layout.addWidget(tabs)
        widget.setLayout(layout)
        return widget
    
    def create_stats_tab(self):
        """
Таб со статистикой
        """
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Прогресс бар
        layout.addWidget(QLabel("Прогресс песни:"))
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)
        
        layout.addSpacing(20)
        
        # Статистика
        stats_grid = QVBoxLayout()
        
        self.score_label = QLabel("Скор: 0")
        self.score_label.setFont(QFont("Arial", 12, QFont.Bold))
        stats_grid.addWidget(self.score_label)
        
        self.accuracy_stats_label = QLabel("Точность: 0%")
        self.accuracy_stats_label.setFont(QFont("Arial", 12, QFont.Bold))
        stats_grid.addWidget(self.accuracy_stats_label)
        
        self.combo_label = QLabel("Комбо: 0")
        self.combo_label.setFont(QFont("Arial", 12, QFont.Bold))
        stats_grid.addWidget(self.combo_label)
        
        self.rank_label = QLabel("Ранг: -")
        self.rank_label.setFont(QFont("Arial", 12, QFont.Bold))
        stats_grid.addWidget(self.rank_label)
        
        layout.addLayout(stats_grid)
        layout.addStretch()
        
        widget.setLayout(layout)
        return widget
    
    def create_logs_tab(self):
        """
Таб с логами
        """
        widget = QWidget()
        layout = QVBoxLayout()
        
        self.logs_text = QTextEdit()
        self.logs_text.setReadOnly(True)
        layout.addWidget(self.logs_text)
        
        widget.setLayout(layout)
        return widget
    
    def create_settings_tab(self):
        """
Таб с настройками
        """
        widget = QWidget()
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel("Путь к FNF:"))
        self.fnf_path_input = QLineEdit()
        layout.addWidget(self.fnf_path_input)
        
        browse_btn = QPushButton("Обзор...")
        layout.addWidget(browse_btn)
        
        layout.addSpacing(20)
        
        layout.addWidget(QLabel("Количество повторов при ошибке:"))
        self.retries_spin = QSpinBox()
        self.retries_spin.setValue(3)
        self.retries_spin.setMinimum(1)
        self.retries_spin.setMaximum(10)
        layout.addWidget(self.retries_spin)
        
        layout.addStretch()
        
        widget.setLayout(layout)
        return widget
