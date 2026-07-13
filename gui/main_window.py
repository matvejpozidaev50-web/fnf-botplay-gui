#!/usr/bin/env python3
"""
Главное окно приложения
"""

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTabWidget, QPushButton, QComboBox, QLabel,
    QTextEdit, QSlider, QCheckBox, QProgressBar,
    QSpinBox, QLineEdit, QFileDialog
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QColor
from utils.config import Config


class MainWindow(QMainWindow):
    def __init__(self, config: Config):
        super().__init__()
        self.config = config
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("FNF BotPlay GUI v1.0")
        self.setGeometry(100, 100, 1200, 800)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()

        # Left panel
        left_panel = self.create_left_panel()
        main_layout.addWidget(left_panel, 1)

        # Right panel
        right_panel = self.create_right_panel()
        main_layout.addWidget(right_panel, 2)

        central_widget.setLayout(main_layout)

    def create_left_panel(self):
        widget = QWidget()
        layout = QVBoxLayout()

        title = QLabel("УПРАВЛЕНИЕ")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        layout.addWidget(title)

        layout.addSpacing(20)

        # Engine selection
        layout.addWidget(QLabel("Двигатель:"))
        self.engine_combo = QComboBox()
        self.engine_combo.addItems(["Psych Engine", "Kade Engine", "v-slice", "Базовый FNF"])
        layout.addWidget(self.engine_combo)

        layout.addSpacing(10)

        # Song selection
        layout.addWidget(QLabel("Песня:"))
        self.song_combo = QComboBox()
        self.song_combo.addItems(["Bopeebo", "Fresh", "Dadbattle"])
        layout.addWidget(self.song_combo)

        layout.addSpacing(10)

        # Difficulty
        layout.addWidget(QLabel("Сложность:"))
        self.difficulty_combo = QComboBox()
        self.difficulty_combo.addItems(["Easy", "Normal", "Hard", "Nightmare"])
        layout.addWidget(self.difficulty_combo)

        layout.addSpacing(10)

        # Start/Stop buttons
        self.start_btn = QPushButton("▶ ЗАПУСТИТЬ")
        self.start_btn.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold; padding: 10px;")
        layout.addWidget(self.start_btn)

        self.stop_btn = QPushButton("⏹ ОСТАНОВИТЬ")
        self.stop_btn.setStyleSheet("background-color: #f44336; color: white; font-weight: bold; padding: 10px;")
        layout.addWidget(self.stop_btn)

        layout.addSpacing(20)

        # Options
        self.record_replay_cb = QCheckBox("Записывать реплеи")
        self.record_replay_cb.setChecked(True)
        layout.addWidget(self.record_replay_cb)

        self.auto_retry_cb = QCheckBox("Автоматический повтор")
        self.auto_retry_cb.setChecked(True)
        layout.addWidget(self.auto_retry_cb)

        layout.addSpacing(20)

        # Accuracy threshold
        layout.addWidget(QLabel("Порог точности (%):"))
        self.accuracy_slider = QSlider(Qt.Horizontal)
        self.accuracy_slider.setMinimum(50)
        self.accuracy_slider.setMaximum(100)
        self.accuracy_slider.setValue(80)
        self.accuracy_slider.valueChanged.connect(self.on_accuracy_changed)
        layout.addWidget(self.accuracy_slider)

        self.accuracy_label = QLabel("80%")
        layout.addWidget(self.accuracy_label)

        layout.addStretch()

        widget.setLayout(layout)
        return widget

    def on_accuracy_changed(self, value):
        self.accuracy_label.setText(f"{value}%")

    def create_right_panel(self):
        widget = QWidget()
        layout = QVBoxLayout()

        tabs = QTabWidget()

        # Stats tab
        stats_widget = self.create_stats_tab()
        tabs.addTab(stats_widget, "📊 Статистика")

        # Logs tab
        logs_widget = self.create_logs_tab()
        tabs.addTab(logs_widget, "📝 Логи")

        # Settings tab
        settings_widget = self.create_settings_tab()
        tabs.addTab(settings_widget, "⚙️ Настройки")

        layout.addWidget(tabs)
        widget.setLayout(layout)
        return widget

    def create_stats_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Прогресс песни:"))
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        layout.addSpacing(20)

        self.score_label = QLabel("Скор: 0")
        self.score_label.setFont(QFont("Arial", 12, QFont.Bold))
        layout.addWidget(self.score_label)

        self.accuracy_stats_label = QLabel("Точность: 0%")
        self.accuracy_stats_label.setFont(QFont("Arial", 12, QFont.Bold))
        layout.addWidget(self.accuracy_stats_label)

        self.combo_label = QLabel("Комбо: 0")
        self.combo_label.setFont(QFont("Arial", 12, QFont.Bold))
        layout.addWidget(self.combo_label)

        self.rank_label = QLabel("Ранг: -")
        self.rank_label.setFont(QFont("Arial", 12, QFont.Bold))
        layout.addWidget(self.rank_label)

        layout.addStretch()

        widget.setLayout(layout)
        return widget

    def create_logs_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        self.logs_text = QTextEdit()
        self.logs_text.setReadOnly(True)
        layout.addWidget(self.logs_text)

        widget.setLayout(layout)
        return widget

    def create_settings_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Путь к FNF:"))
        self.fnf_path_input = QLineEdit()
        self.fnf_path_input.setText(str(self.config.fnf_path))
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
