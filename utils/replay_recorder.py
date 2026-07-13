#!/usr/bin/env python3
"""
Запись реплеев
"""

import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any
from dataclasses import dataclass, asdict


@dataclass
class KeyPress:
    """Нажатие клавиши"""
    timestamp: float
    key: str
    pressed: bool
    note_accuracy: float = 0.0
    note_type: str = ""


class ReplayRecorder:
    """Запись реплеев игры"""

    def __init__(self, replay_dir: str = "replays"):
        self.replay_dir = Path(replay_dir)
        self.replay_dir.mkdir(exist_ok=True)
        self.key_presses: List[KeyPress] = []
        self.session_start: datetime = datetime.now()

    def record_key_press(
        self,
        key: str,
        pressed: bool,
        timestamp: float,
        accuracy: float = 0.0,
        note_type: str = "",
    ) -> None:
        """
        Записать нажатие клавиши

        Args:
            key: Код клавиши
            pressed: True если нажата, False если отпущена
            timestamp: Временная метка события
            accuracy: Точность попадания по ноте
            note_type: Тип ноты (normal, hold, alt, etc)
        """
        key_press = KeyPress(
            timestamp=timestamp,
            key=key,
            pressed=pressed,
            note_accuracy=accuracy,
            note_type=note_type,
        )
        self.key_presses.append(key_press)

    def save_replay(
        self,
        song_name: str,
        difficulty: str,
        engine: str,
        final_score: int,
        final_accuracy: float,
        max_combo: int,
    ) -> Path:
        """
        Сохранить реплей в файл

        Args:
            song_name: Название песни
            difficulty: Сложность
            engine: Двигатель FNF
            final_score: Финальный скор
            final_accuracy: Финальная точность
            max_combo: Максимальное комбо

        Returns:
            Path к сохраненному файлу
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{song_name}_{difficulty}_{engine}_{timestamp}.json"
        filepath = self.replay_dir / filename

        replay_data = {
            "metadata": {
                "song_name": song_name,
                "difficulty": difficulty,
                "engine": engine,
                "timestamp": str(self.session_start),
                "duration_seconds": len(self.key_presses),
            },
            "statistics": {
                "final_score": final_score,
                "final_accuracy": final_accuracy,
                "max_combo": max_combo,
            },
            "key_presses": [asdict(kp) for kp in self.key_presses],
        }

        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(replay_data, f, indent=2, ensure_ascii=False)
            print(f"[*] Реплей сохранен: {filepath}")
        except Exception as e:
            print(f"[!] Ошибка сохранения реплея: {e}")

        return filepath

    def clear(self) -> None:
        """Очистить записанные события"""
        self.key_presses.clear()
        self.session_start = datetime.now()
