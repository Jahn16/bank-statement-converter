from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import convert

app = FastAPI(
    title="Fatura2Csv",
    version="0.1.0",
    description="Aplicação para converter faturas em PDF para CSV",
)


# TODO: make a setting class to store origins
origins = ["http://localhost:3000", "localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(convert.router)
