from fastapi import APIRouter, UploadFile

router = APIRouter()


@router.post("/pdf_to_csv")
async def convert_pdf_to_csv(file: UploadFile) -> dict[str, str]:
    return {"filename": file.filename or ""}
