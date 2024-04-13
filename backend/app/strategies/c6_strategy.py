import re

import structlog

from app.entities.pdf_reader import PDFReader
from app.strategies.parser_strategy import ParserStrategy

logger = structlog.get_logger()


class C6Parser(ParserStrategy):
    regex_pattern = r"(\d{2}\/\d{2}\/\d{4})\s([\w\s]+)-?([\w\s]+)?\s(?:\d+)\s([0-9,]+)\s([CD])"  # noqa: E501

    def parse_line(self, line: str) -> dict[str, str]:
        matches = re.match(self.regex_pattern, line)
        if not matches:
            return {}
        transaction_type = matches.group(5)
        value = matches.group(4)
        return {
            "Data": matches.group(1),
            "Descricão": matches.group(2),
            "Conta": matches.group(3) or "",
            "Valor": value if transaction_type == "C" else f"-{value}",
        }

    def parse_transactions(
        self, pdf_reader: PDFReader
    ) -> list[dict[str, str]]:
        pages = pdf_reader.get_pages()
        text = pdf_reader.extract_text(pages)
        lines = text.splitlines()
        transactions_lines = list(filter(super()._is_transaction, lines))
        transactions = list(map(self.parse_line, transactions_lines))
        return transactions
