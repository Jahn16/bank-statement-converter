import re
from abc import ABC, abstractmethod

from app.entities.pdf_reader import PDFReader


class ParserStrategy(ABC):
    regex_pattern: str

    def _is_transaction(self, line: str) -> bool:
        return bool(re.match(self.regex_pattern, line, re.UNICODE))

    @abstractmethod
    def parse_transactions(
        self, pdf_reader: PDFReader
    ) -> list[dict[str, str]]:
        raise NotImplementedError
