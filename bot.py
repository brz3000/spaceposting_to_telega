import os
import time
from dotenv import load_dotenv
import telegram
import random
import argparse


def post_image(bot, image_path):
    bot.send_document(chat_id=chat_id, document=open(image_path, 'rb'))
    return


def generate_images_path():
    images_path = []
    for root, dirs, files in os.walk("./images"):
        for name in files:
            images_path.append(os.path.join(root, name))
    random.shuffle(images_path)
    return images_path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--timeout", type=int, help="Введите через какое количество минут постить")
    args = parser.parse_args()
    load_dotenv()
    token = os.environ['TLG_TOKEN']
    chat_id = os.environ['TLG_CHAT_ID']
    delay = os.environ['DELAY']
    bot = telegram.Bot(token)
    if args.timeout:
        delay = args.timeout
    while True:
        for image_path in generate_images_path():
            post_image(bot, image_path)
            time.sleep(60*int(delay))
