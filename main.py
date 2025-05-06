from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import property_lookup
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# ✅ CORS configuration
origins = [
    "http://localhost:3000",                 # Local React dev server
    "https://your-frontend-url.com"          # 🔁 Replace with your real deployed frontend domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Register your property lookup route
app.include_router(property_lookup.router)

@app.get("/")
def root():
    return {"message": "CMA API is running"}
