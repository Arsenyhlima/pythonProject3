import os
import requests
from datetime import datetime
from download_picture import download_picture 


def fetch_epic_nasa(nasa_count, api_key):
    params = {
        "api_key": api_key,
        "count": nasa_count,
    }
    response = requests.get("https://api.nasa.gov/EPIC/api/natural/image", params=params)
    response.raise_for_status()
    urls = response.json()
    for image_url in urls:
        image = image_url["image"]
        image_date = image_url["date"]
        image_date = datetime.fromisoformat(image_date).strftime("%Y/%m/%d")
        epic_url = f"https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image}.png"
        path = os.path.join("images", f"{image}.png")
        download_picture(epic_url, path, params)


def main():
    nasa_count = 30
    api_key = os.environ['NASA_TOKEN']
    fetch_epic_nasa(nasa_count, api_key)


if __name__ == "__main__":
    main()
    
