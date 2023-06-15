import os
import time
from dotenv import load_dotenv
import telegram
import random
import argparse


def post_image(bot, image_path):
    with open(image_path, 'rb') as file_handler:
        photo = file_handler.read()
        bot.send_document(chat_id=chat_id, document=photo)
    return


def generate_images_path():
    image_paths = []
    for root, dirs, files in os.walk("./images"):
        for name in files:
            image_paths.append(os.path.join(root, name))
    random.shuffle(image_paths)
    return image_paths


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''<Bot for auto POST image to telegram every 240 min by default.
                                                 Use --timeout argument for change timeout. Example use
                                                 "python bot.py --timeout 1"
                                                 for post image every one minutes>''')
    parser.add_argument("--timeout", default='240', type=int, help="Enter in how many minutes to post")
    args = parser.parse_args()
    load_dotenv()
    token = os.environ['TLG_TOKEN']
    chat_id = os.environ['TLG_CHAT_ID']
    bot = telegram.Bot(token)
    while True:
        for image_path in generate_images_path():
            post_image(bot, image_path)
            time.sleep(60*int(args.timeout))
