import requests
import os
from pathlib import Path
from dotenv import load_dotenv
from download_image import download_image
import fetch_epic_images
import fetch_spacex_images
import fetch_apod_images
import argparse


if __name__ == '__main__':
    Path("./images").mkdir(parents=True, exist_ok=True)
    if not os.path.exists("./images"):
        os.makedirs("./images")
    load_dotenv()
    token = os.environ['NASA_TOKEN']
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", default='latest', type=str, help="Введите id запуска")
    args = parser.parse_args()

    for image_number, image_url in enumerate(fetch_spacex_images.get_images_list_from_spacex(args.l)):
        filename = f'./images/spacex{image_number}.jpeg'
        download_image(image_url, filename)
    for image_number, image_url in enumerate(fetch_apod_images.get_apod_image_list(token)):
        filename = f'./images/nasa_apod_{image_number}{fetch_apod_images.get_extention_from_url(image_url)}'
        download_image(image_url, filename)
    for image_number, image_url in enumerate(fetch_epic_images.get_epic_image_list(token)):
        image_url = f'{image_url}?api_key={token}'
        filename = f'./images/nasa_epic_{image_number}.png'
        download_image(image_url, filename)
