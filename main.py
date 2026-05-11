from fastapi import FastAPI
from app.routers.chrome_routers import router

app = FastAPI(debug= True, title="API para gerenciar chromebooks do colegio", servers=[{"url": "http://127.0.0.1:8000", "description": "Dev Environment"}])

app.include_router(router)
