#!/usr/bin/env python3
"""
Поддержка Kade Engine
"""

from pathlib import Path
from typing import Dict, List
from engines.base_engine import BaseEngine


class KadeEngine(BaseEngine):
    """Двигатель Kade Engine"""

    def __init__(self, path: Path):
        super().__init__(path)
        self.name = "Kade Engine"

    def get_songs(self) -> List[str]:
        """Получить список песен"""
        return ["Bopeebo", "Fresh", "Dadbattle"]

    def get_difficulties(self, song: str) -> List[str]:
        """Получить сложности"""
        return ["Easy", "Normal", "Hard", "Nightmare"]

    def get_chart(self, song: str, difficulty: str) -> Dict:
        """Получить чарт"""
        return {"notes": []}

    def get_mods(self) -> List[str]:
        """Получить моды"""
        return []
