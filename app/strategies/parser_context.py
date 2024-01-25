from app.entities.pdf_reader import PDFReader
from app.strategies.parser_strategy import ParserStrategy


class ParserContext:
    def set_strategy(self, strategy: ParserStrategy) -> None:
        self.strategy = strategy

    def parse_transactions(
        self, pdf_reader: PDFReader
    ) -> list[dict[str, str]]:
        return self.strategy.parse_transactions(pdf_reader)
