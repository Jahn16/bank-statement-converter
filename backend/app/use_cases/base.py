from abc import ABC, abstractmethod
from typing import Any, BinaryIO


class BaseUseCase(ABC):
    @abstractmethod
    def execute(self, file: BinaryIO, bank: str) -> Any:
        pass
