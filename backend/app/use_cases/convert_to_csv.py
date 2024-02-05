from io import BytesIO, StringIO
from typing import BinaryIO

import structlog

from app.entities.csv_writer import CsvWriter
from app.entities.pdf_reader import PDFReader
from app.exceptions.bank import BankNotSupported
from app.strategies.inter_parser import InterParser
from app.strategies.parser_context import ParserContext
from app.use_cases.base import BaseUseCase

logger = structlog.get_logger()


class ConvertToCsv(BaseUseCase):
    def execute(self, file: BinaryIO, bank: str) -> StringIO:
        pdf_reader = PDFReader(BytesIO(file.read()))
        parser_context = ParserContext()
        if bank.lower() == "inter":
            parser_context.set_strategy(InterParser())
        else:
            logger.warning("Requested bank not supported", bank=bank)
            raise BankNotSupported(bank)
        logger.info("Initiated fileparse", bank=bank, filename=file.name)
        transactions = parser_context.parse_transactions(pdf_reader)
        logger.info("Finished parsing file", bank=bank, filename=file.name)
        return CsvWriter.write(transactions)
