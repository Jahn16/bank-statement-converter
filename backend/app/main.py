from fastapi import FastAPI

from app.routers import convert

app = FastAPI(
    title="Fatura2Csv",
    version="0.1.0",
    description="Aplicação para converter faturas em PDF para CSV",
)

app.include_router(convert.router)
