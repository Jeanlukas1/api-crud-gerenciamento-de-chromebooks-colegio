from app.db.db_connection import chrome_collection

def create_chrome_repository(chrome: dict):
    return chrome_collection.insert_one(chrome)
    
