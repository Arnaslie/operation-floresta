import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOPOGRAPHY_KEY=os.environ.get('OPEN_TOPOGRAPHY')

url = "https://portal.opentopography.org/API/globaldem"
params = {
    "demtype": "SRTMGL1",         # DEM dataset (e.g., SRTMGL1, SRTM15Plus, etc.)
    "south": -6.8345,
    "north": -4.9633,
    "west": -53.1037,
    "east": -51.722,
    "outputFormat": "GTiff",       # GeoTIFF format
    "API_Key": TOPOGRAPHY_KEY # API key
}

response = requests.get(url, params=params)

# Save file if successful
if response.status_code == 200:
    with open("region_dem.tif", "wb") as f:
        f.write(response.content)
    print("TIFF file downloaded.")
else:
    print("Failed:", response.text)
