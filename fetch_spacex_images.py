import requests
import argparse
from download_picture import download_picture


def fetch_spacex_last_launch(url):
    response = requests.get(url)
    response.raise_for_status()
    for response_link in response.json():
        url_photos = response_link["links"]["flickr"]["original"]
        for number, url_photo in enumerate(url_photos):
            filename = f"images/spacex{number}.jpg"
            download_picture(url_photo, filename)


def main():
    launch_id = "5eb87d47ffd86e000604b38a"
    parser = argparse.ArgumentParser(description="Этот скрипт загружает фото от SpaceX по указанному id запуска")
    parser.add_argument('--id', default=launch_id, help='id запуска, по которому загружается фото от SpaceX', dest="id")
    args = parser.parse_args()
    fetch_spacex_last_launch(args.id)


if __name__ == "__main__":
    main()
