#!/usr/bin/env python3
"""
Основная логика бота для автоматического прохождения FNF
"""

import time
from typing import List, Dict, Optional
from enum import Enum


class Direction(Enum):
    LEFT = "left"
    DOWN = "down"
    UP = "up"
    RIGHT = "right"


class NoteType(Enum):
    NORMAL = "normal"
    HOLD = "hold"
    ALT = "alt"


class BotPlay:
    """Основной класс для автоматического прохождения FNF"""

    KEY_MAP = {
        Direction.LEFT: "a",
        Direction.DOWN: "s",
        Direction.UP: "w",
        Direction.RIGHT: "d",
    }

    def __init__(self, accuracy_threshold: float = 0.8):
        self.accuracy_threshold = accuracy_threshold
        self.is_running = False
        self.notes: List[Dict] = []
        print(f"[*] BotPlay инициализирован с порогом точности: {accuracy_threshold * 100}%")

    def load_chart(self, chart_data: Dict) -> None:
        """Загрузить чарт песни"""
        self.notes = chart_data.get("notes", [])
        print(f"[*] Чарт загружен с {len(self.notes)} нотами")

    def start(self) -> None:
        """Начать автоматическое прохождение"""
        self.is_running = True
        print("[*] BotPlay запущен")

    def stop(self) -> None:
        """Остановить автоматическое прохождение"""
        self.is_running = False
        print("[*] BotPlay остановлен")

    def press_key(self, direction: Direction) -> None:
        """Нажать клавишу"""
        key = self.KEY_MAP.get(direction)
        if key:
            print(f"[*] Нажимаю клавишу: {key}")

    def release_key(self, direction: Direction) -> None:
        """Отпустить клавишу"""
        key = self.KEY_MAP.get(direction)
        if key:
            print(f"[*] Отпускаю клавишу: {key}")
