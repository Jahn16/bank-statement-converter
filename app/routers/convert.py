from fastapi import APIRouter, UploadFile
from fastapi.responses import StreamingResponse

from app.entities.csv_writer import CsvWriter
from app.entities.pdf_reader import PDFReader
from app.strategies.inter_parser import InterParser

router = APIRouter()


@router.post("/pdf_to_csv")
def convert_pdf_to_csv(file: UploadFile) -> StreamingResponse:
    # TODO: Validate if the file is PDF
    pdf_reader = PDFReader(file.file)  # pyright: ignore
    parser = InterParser()
    transactions = parser.parse_transactions(pdf_reader)
    result = CsvWriter.write(transactions)
    response = StreamingResponse(
        iter([result.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=fatura.csv"},
    )
    return response
