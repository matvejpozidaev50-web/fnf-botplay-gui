#!/usr/bin/env python3
"""
Поддержка v-slice Engine
"""

from pathlib import Path
from typing import Dict, List
from engines.base_engine import BaseEngine


class VSliceEngine(BaseEngine):
    """Двигатель v-slice"""

    def __init__(self, path: Path):
        super().__init__(path)
        self.name = "v-slice Engine"

    def get_songs(self) -> List[str]:
        """Получить список песен"""
        return ["Bopeebo"]

    def get_difficulties(self, song: str) -> List[str]:
        """Получить сложности"""
        return ["Easy", "Normal", "Hard"]

    def get_chart(self, song: str, difficulty: str) -> Dict:
        """Получить чарт"""
        return {"notes": []}

    def get_mods(self) -> List[str]:
        """Получить моды"""
        return []
