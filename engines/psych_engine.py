#!/usr/bin/env python3
"""
Поддержка Psych Engine
"""

import json
from pathlib import Path
from typing import Dict, List
from engines.base_engine import BaseEngine


class PsychEngine(BaseEngine):
    """Двигатель Psych Engine"""

    def __init__(self, path: Path):
        super().__init__(path)
        self.name = "Psych Engine"
        self.data_path = self.path / "assets" / "data"

    def get_songs(self) -> List[str]:
        """Получить список песен из Psych Engine"""
        songs = []
        if self.data_path.exists():
            for file in self.data_path.glob("*.json"):
                if not file.name.startswith("_"):
                    songs.append(file.stem)
        return sorted(songs)

    def get_difficulties(self, song: str) -> List[str]:
        """Получить сложности для песни"""
        return ["Easy", "Normal", "Hard"]

    def get_chart(self, song: str, difficulty: str) -> Dict:
        """Получить чарт песни"""
        return {"notes": []}

    def get_mods(self) -> List[str]:
        """Получить список модов"""
        mods_dir = self.path / "mods"
        if mods_dir.exists():
            return [d.name for d in mods_dir.iterdir() if d.is_dir()]
        return []
