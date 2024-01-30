from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import convert
from app.settings import Settings

app = FastAPI(
    title="Fatura2Csv",
    version="0.1.0",
    description="Aplicação para converter faturas em PDF para CSV",
)


settings = Settings()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.backend_cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(convert.router)
