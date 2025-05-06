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
            "query": f"address:\"{address}\"",
            "format": "JSON",
            "num_records": 1,
            "product": "property"
        }

        print("🔍 Searching with v3 for:", address)
        print("🔧 Query params:", params)

        response = requests.get("https://api.datafiniti.net/v3/data", headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        if not data.get("records"):
            return JSONResponse(content={"message": "No records found in v3."}, status_code=404)

        return data

    except requests.HTTPError as e:
        print("❌ HTTP error:", e.response.status_code, e.response.text)
        return JSONResponse(content={"error": f"Datafiniti error {e.response.status_code}", "details": e.response.text}, status_code=502)

    except Exception as e:
        print("❌ General error:", str(e))
        return JSONResponse(content={"error": "Internal server error"}, status_code=500)
