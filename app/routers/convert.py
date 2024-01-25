from fastapi import APIRouter, HTTPException, UploadFile
from fastapi.responses import StreamingResponse

from app.use_cases.convert_to_csv import ConvertToCsv

router = APIRouter()


@router.post("/pdf_to_csv")
def convert_pdf_to_csv(file: UploadFile) -> StreamingResponse:
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="The file must be a pdf")

    convert_use_case = ConvertToCsv()
    result = convert_use_case.execute(file.file)
    response = StreamingResponse(
        iter([result.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=fatura.csv"},
    )
    return response
