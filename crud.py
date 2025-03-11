# crud.py
import random
import string
from database import get_session

def generate_short_code(length=6):
    """Generates a random short code (6 characters)"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_short_url(long_url: str):
    """Inserts a new short URL into Snowflake"""
    session = get_session()
    short_code = generate_short_code()

    # Ensure uniqueness
    while session.sql(f"SELECT COUNT(*) FROM PROD_PERSONAL_DB.ANISH_KUMAR.URLS WHERE short_code = '{short_code}'").collect()[0][0] > 0:
        short_code = generate_short_code()  # Regenerate if duplicate

    session.sql(f"""
        INSERT INTO PROD_PERSONAL_DB.ANISH_KUMAR.URLS (short_code, long_url, clicks)
        VALUES ('{short_code}', '{long_url}', 0)
    """).collect()
    
    return {"short_code": short_code, "long_url": long_url}

def get_long_url(short_code: str):
    """Fetches the original long URL using the short code"""
    session = get_session()
    result = session.sql(f"SELECT long_url FROM PROD_PERSONAL_DB.ANISH_KUMAR.URLS WHERE short_code = '{short_code}'").collect()
    
    if result:
        return {"long_url": result[0][0]}
    return {"error": "Short URL not found"}

def increment_click_count(short_code: str):
    """Increments the click count for a short URL"""
    session = get_session()
    session.sql(f"""
        UPDATE PROD_PERSONAL_DB.ANISH_KUMAR.URLS 
        SET clicks = clicks + 1 
        WHERE short_code = '{short_code}'
    """).collect()
