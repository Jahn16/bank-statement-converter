from abc import ABC, abstractmethod

from app.entities.pdf_reader import PDFReader


class ParserStrategy(ABC):
    @abstractmethod
    def parse_transactions(
        self, pdf_reader: PDFReader
    ) -> list[dict[str, str]]:
        pass
