from app.repositories.chrome_repository import *
from app.models.chromebooks_model import *

def create_service(chrome:ChromeBookModel) -> dict:
    data = create_chrome_repository(chrome)

    return {
        "message": "Chrome Created!",
        "info": data
    }