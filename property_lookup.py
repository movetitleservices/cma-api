from fastapi import APIRouter, Query
import requests
import os

router = APIRouter()

@router.get("/property-lookup")
def property_lookup(address: str = Query(...)):
    headers = {
        "Authorization": f"Bearer {os.getenv('DATAFINITI_API_KEY')}"
    }
    params = {
        "query": f"address:\"{address}\"",
        "format": "JSON",
        "num_records": 1
    }
    response = requests.get("https://api.datafiniti.co/v4/properties/search", headers=headers, params=params)
    return response.json()
