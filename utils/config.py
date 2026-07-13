#!/usr/bin/env python3
"""
Конфигурация приложения
"""

import json
from pathlib import Path
from typing import Any, Dict


class BotConfig:
    """Конфигурация бота"""
    def __init__(self):
        self.engine = "psych"
        self.accuracy_threshold = 0.8
        self.auto_retry = True
        self.max_retries = 3
        self.record_replays = True


class GUIConfig:
    """Конфигурация GUI"""
    def __init__(self):
        self.window_width = 1200
        self.window_height = 800
        self.theme = "dark"
        self.auto_start = False


class Config:
    """Главная конфигурация приложения"""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = Path(config_path)
        self.bot = BotConfig()
        self.gui = GUIConfig()
        self.fnf_path = Path.home() / "FNF"

        if self.config_path.exists():
            self.load()
        else:
            self.save()

    def load(self) -> None:
        """Загрузить конфигурацию из файла"""
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            if "bot" in data:
                for key, value in data["bot"].items():
                    if hasattr(self.bot, key):
                        setattr(self.bot, key, value)

            if "gui" in data:
                for key, value in data["gui"].items():
                    if hasattr(self.gui, key):
                        setattr(self.gui, key, value)

            if "fnf_path" in data:
                self.fnf_path = Path(data["fnf_path"])

            print(f"[*] Конфигурация загружена из: {self.config_path}")
        except Exception as e:
            print(f"[!] Ошибка загрузки конфигурации: {e}")

    def save(self) -> None:
        """Сохранить конфигурацию в файл"""
        try:
            data = {
                "bot": {
                    "engine": self.bot.engine,
                    "accuracy_threshold": self.bot.accuracy_threshold,
                    "auto_retry": self.bot.auto_retry,
                    "max_retries": self.bot.max_retries,
                    "record_replays": self.bot.record_replays,
                },
                "gui": {
                    "window_width": self.gui.window_width,
                    "window_height": self.gui.window_height,
                    "theme": self.gui.theme,
                    "auto_start": self.gui.auto_start,
                },
                "fnf_path": str(self.fnf_path),
            }
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"[*] Конфигурация сохранена в: {self.config_path}")
        except Exception as e:
            print(f"[!] Ошибка сохранения конфигурации: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        """Получить значение из конфигурации"""
        keys = key.split(".")
        if keys[0] == "bot":
            obj = self.bot
        elif keys[0] == "gui":
            obj = self.gui
        else:
            return default

        try:
            for k in keys[1:]:
                obj = getattr(obj, k)
            return obj
        except AttributeError:
            return default

    def set(self, key: str, value: Any) -> None:
        """Установить значение в конфигурацию"""
        keys = key.split(".")
        if keys[0] == "bot":
            obj = self.bot
        elif keys[0] == "gui":
            obj = self.gui
        else:
            return

        try:
            for k in keys[1:-1]:
                obj = getattr(obj, k)
            setattr(obj, keys[-1], value)
            self.save()
        except AttributeError:
            pass
