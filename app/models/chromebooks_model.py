from pydantic import BaseModel

class ChromeBookModel(BaseModel):
    email: str
    password: str
