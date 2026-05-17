from app.repositories.chrome_repository import *
from app.models.chromebooks_model import *


def to_dict(chrome: ChromeBookModel) -> dict:
    return chrome.model_dump(mode="json")

def create_service(chrome: ChromeBookModel) -> dict:
    data = to_dict(chrome)
    result = create_chrome_repository(data)
        
    return {
        "message": "Chrome Created",
        "id": str(result.inserted_id)
        }
