import os
from os import listdir
import telegram
from time import sleep
import random
from fetch_epic_nasa import fetch_epic_nasa
from nasa_get import nasa_get


def main():
    count_nasa = 30
    count_url = 5
    api_key = os.environ['NASA_TOKEN']
    fetch_epic_nasa(count_url, api_key)
    nasa_get(count_nasa, api_key)
    os.makedirs("images", exist_ok=True)
    telegram_token = os.environ['TG_TOKEN']
    time = os.environ["TIME_REPEAT"]
    default_time = 14400
    time_repeat = os.environ.get(time, default_time)
    telegram_id = os.environ["TG_CHAT_ID"]
    bot = telegram.Bot(token=telegram_token)
    while True:
        folder = "images"
        files = listdir(folder)
        random.shuffle(files)
        for image in files:
            filepath = os.path.join(files, image)
            with open(filepath, "rb") as f:
                bot.send_document(chat_id=telegram_id, document=f)
        sleep(time_repeat)


if __name__ == "__main__":
    main()
