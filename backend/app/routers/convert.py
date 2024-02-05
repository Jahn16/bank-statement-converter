from typing import Annotated

import structlog
from fastapi import APIRouter, Form, HTTPException, UploadFile
from fastapi.responses import StreamingResponse

from app.exceptions.bank import BankNotSupported
from app.use_cases.convert_to_csv import ConvertToCsv

logger = structlog.get_logger()
router = APIRouter()


@router.post("/pdf_to_csv")
def convert_pdf_to_csv(
    file: UploadFile, bank: Annotated[str, Form()]
) -> StreamingResponse:
    if file.content_type != "application/pdf":
        logger.warning(
            "File type not supported", content_type=file.content_type
        )
        raise HTTPException(status_code=400, detail="The file must be a pdf")

    convert_use_case = ConvertToCsv()
    try:
        result = convert_use_case.execute(file.file, bank)
    except BankNotSupported as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        logger.exception("Could not process csv")
        raise HTTPException(
            status_code=500, detail="Could not generate CSV file"
        )
    response = StreamingResponse(
        iter([result.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=fatura.csv"},
    )
    return response
