from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import property_lookup
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://your-frontend-url.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(property_lookup.router)

@app.get("/")
def root():
    return {"message": "CMA API is running"}
