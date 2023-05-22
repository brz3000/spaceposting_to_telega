import requests
import os
from pathlib import Path
from dotenv import load_dotenv
from main import download_image
import argparse


def get_images_list_from_spacex(launch=''):
    url_template = 'https://api.spacexdata.com/v5/launches/{}'
    if not launch:
        launch = 'latest'
    url = url_template.format(launch)
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


if __name__ == '__main__':
    Path("./images").mkdir(parents=True, exist_ok=True)
    if not os.path.exists("./images"):
        os.makedirs("./images")
    load_dotenv()
    token = os.environ['NASA_TOKEN']
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", default='latest', type=str, help="Введите id запуска")
    args = parser.parse_args()

    for image_number, image_url in enumerate(get_images_list_from_spacex(args.l)):
        filename = f'./images/spacex{image_number}.jpeg'
        download_image(image_url, filename)
