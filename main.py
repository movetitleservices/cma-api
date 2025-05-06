from fastapi import FastAPI
from routers import property_lookup
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
app.include_router(property_lookup.router)

@app.get("/")
def root():
    return {"message": "CMA API is running"}
