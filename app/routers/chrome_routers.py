from fastapi import APIRouter, HTTPException
from app.services.chrome_service import *
from app.models.chromebooks_model import *

router = APIRouter()

@router.post("/chrome")
def create_chrome(chrome:ChromeBookModel):
    return create_service(chrome)
