from typing import Annotated

from fastapi import APIRouter, Form, HTTPException, UploadFile
from fastapi.responses import StreamingResponse

from app.exceptions.bank import BankNotSupported
from app.use_cases.convert_to_csv import ConvertToCsv

router = APIRouter()


@router.post("/pdf_to_csv")
def convert_pdf_to_csv(
    file: UploadFile, bank: Annotated[str, Form()]
) -> StreamingResponse:
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="The file must be a pdf")

    convert_use_case = ConvertToCsv()
    try:
        result = convert_use_case.execute(file.file, bank)
    except BankNotSupported as e:
        raise HTTPException(status_code=400, detail=str(e))
    response = StreamingResponse(
        iter([result.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=fatura.csv"},
    )
    return response
