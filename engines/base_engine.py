#!/usr/bin/env python3
"""
Базовый класс для двигателей FNF
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, List


class BaseEngine(ABC):
    """Базовый класс для всех двигателей FNF"""

    def __init__(self, path: Path):
        self.path = Path(path)
        self.name = "Base FNF"
        print(f"[*] Инициализирован {self.name}")

    @abstractmethod
    def get_songs(self) -> List[str]:
        """Получить список доступных песен"""
        pass

    @abstractmethod
    def get_difficulties(self, song: str) -> List[str]:
        """Получить сложности для песни"""
        pass

    @abstractmethod
    def get_chart(self, song: str, difficulty: str) -> Dict:
        """Получить чарт песни"""
        pass

    @abstractmethod
    def get_mods(self) -> List[str]:
        """Получить список модов"""
        pass
