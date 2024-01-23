from fastapi import APIRouter, UploadFile

from app.entities.pdf_reader import PDFReader

router = APIRouter()


@router.post("/pdf_to_csv")
async def convert_pdf_to_csv(file: UploadFile) -> str:
    pdf_reader = PDFReader(file.file)  # pyright: ignore
    return pdf_reader.extract_text([1, 2])
