from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
import requests
import os

router = APIRouter()

@router.get("/property-lookup")
def property_lookup(address: str = Query(...)):
    try:
        headers = {
            "Authorization": f"Bearer {os.getenv('DATAFINITI_API_KEY')}"
        }
        params = {
            "query": f"address:{address}",
            "format": "JSON",
            "num_records": 1
        }

        print("🔍 Searching for:", address)
        print("🔧 Query sent:", params)

        response = requests.get("https://api.datafiniti.co/v4/properties/search", headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        if "records" not in data or not data["records"]:
            return JSONResponse(content={"message": "No records found."}, status_code=404)

        return data

    except requests.RequestException as e:
        print("❌ Request to Datafiniti failed:", str(e))
        return JSONResponse(content={"error": "Failed to contact Datafiniti."}, status_code=502)

    except Exception as e:
        print("❌ Unexpected error:", str(e))
        return JSONResponse(content={"error": "Internal server error."}, status_code=500)
