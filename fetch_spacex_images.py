import requests
import argparse
from download_picture import download_picture


def fetch_spacex_last_launch(launch_id):
    if launch_id:
        url = f"https://api.spacexdata.com/v4/launches/{launch_id}"
    else:
        url = "https://api.spacexdata.com/v4/launches/latest"
    response = requests.get(url)
    response.raise_for_status()
    if launch_id:
        url_photos = response.json()["links"]["flickr"]["original"]
    else:
        url_photos = []
        for response_link in response.json():
            if response_link["links"]["flickr"]["original"]:
                url_photos.append(response_link["links"]["flickr"]["original"])
        print(url_photos)
    for number, url_photo in enumerate(url_photos):
        filename = f"images/spacex{number}.jpg"
        download_picture(url_photo, filename)


def main():
     parser = argparse.ArgumentParser(description="Этот скрипт загружает фото от SpaceX по указанному id запуска")
     parser.add_argument('--id', dest='launch_id', default='5eb87d47ffd86e000604b38a', help='id запуска, по которому загружается фото от SpaceX')
     args = parser.parse_args()
     fetch_spacex_last_launch(args.launch_id)


if __name__ == "__main__":
    main()
