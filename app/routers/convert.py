from fastapi import APIRouter, UploadFile
from fastapi.responses import StreamingResponse

from app.use_cases.convert_to_csv import ConvertToCsv

router = APIRouter()


@router.post("/pdf_to_csv")
def convert_pdf_to_csv(file: UploadFile) -> StreamingResponse:
    # TODO: Validate if the file is PDF
    convert_use_case = ConvertToCsv()
    result = convert_use_case.execute(file.file)
    response = StreamingResponse(
        iter([result.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=fatura.csv"},
    )
    return response
