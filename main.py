from crud import create_short_url, get_long_url,generate_short_code,increment_click_count
from fastapi import FastAPI,Depends
from database import get_session
from pydantic import BaseModel

class URLRequest(BaseModel):
    long_url: str

app=FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/shorten/")
def shorten_url(request: URLRequest,session=Depends(get_session)):
    return create_short_url(request.long_url)

@app.get("/{short_code}")
def redirect_to_url(short_code: str, session=Depends(get_session)):
    """Fetches the long URL and increments click count"""
    url_data = get_long_url(short_code)
    
    if "error" in url_data:
        return url_data
    
    increment_click_count(short_code)
    return url_data