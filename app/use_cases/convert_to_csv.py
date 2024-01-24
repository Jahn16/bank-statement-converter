from io import StringIO
from typing import BinaryIO

from app.entities.csv_writer import CsvWriter
from app.entities.pdf_reader import PDFReader
from app.strategies.inter_parser import InterParser
from app.use_cases.base import BaseUseCase


class ConvertToCsv(BaseUseCase):
    def execute(self, file: BinaryIO) -> StringIO:
        pdf_reader = PDFReader(file)  # type: ignore
        parser = InterParser()
        transactions = parser.parse_transactions(pdf_reader)
        return CsvWriter.write(transactions)
