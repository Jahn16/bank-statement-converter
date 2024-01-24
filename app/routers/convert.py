from fastapi import APIRouter, UploadFile

from app.entities.pdf_reader import PDFReader
from app.strategies.inter_parser import InterParser

router = APIRouter()


@router.post("/pdf_to_csv")
async def convert_pdf_to_csv(file: UploadFile) -> list[dict[str, str]]:
    # TODO: Validate if the file is PDF
    pdf_reader = PDFReader(file.file)  # pyright: ignore
    parser = InterParser()
    return parser.parse_transactions(pdf_reader)
