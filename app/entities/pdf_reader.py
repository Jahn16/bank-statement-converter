import io

from pdfminer.high_level import extract_pages, extract_text
from pdfminer.layout import LAParams


class PDFReader:
    def __init__(self, file: io.BytesIO):
        self.file = file

    def extract_text(self, pages: list[int]) -> str:
        return (
            extract_text(
                self.file,
                page_numbers=pages,
                laparams=LAParams(boxes_flow=None, char_margin=100),
            )
            or ""
        )

    def get_pages(self) -> list[int]:
        return [page.pageid - 1 for page in extract_pages(self.file)]
