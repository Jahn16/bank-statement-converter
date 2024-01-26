from io import StringIO
from typing import BinaryIO

from app.entities.csv_writer import CsvWriter
from app.entities.pdf_reader import PDFReader
from app.exceptions.bank import BankNotSupported
from app.strategies.inter_parser import InterParser
from app.strategies.parser_context import ParserContext
from app.use_cases.base import BaseUseCase


class ConvertToCsv(BaseUseCase):
    def execute(self, file: BinaryIO, bank: str) -> StringIO:
        pdf_reader = PDFReader(file)  # type: ignore
        parser_context = ParserContext()
        if bank.lower() == "inter":
            parser_context.set_strategy(InterParser())
        else:
            raise BankNotSupported(bank)
        transactions = parser_context.parse_transactions(pdf_reader)
        return CsvWriter.write(transactions)
