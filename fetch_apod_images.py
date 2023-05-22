import requests
import os
from pathlib import Path
from dotenv import load_dotenv
from main import download_image
from urllib.parse import urlparse


def get_extention_from_url(url):
    url_elements = urlparse(url)
    extention = os.path.splitext(url_elements.path)[1]
    return f'{extention}'


def get_apod_image_list(token, count=30):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': token, 'count': count}
    response = requests.get(url, params=params)
    response.raise_for_status()
    apod_url_list = []
    for apod in response.json():
        apod_url_list.append(apod['url'])
    return apod_url_list


if __name__ == '__main__':
    Path("./images").mkdir(parents=True, exist_ok=True)
    if not os.path.exists("./images"):
        os.makedirs("./images")
    load_dotenv()
    token = os.environ['NASA_TOKEN']

    for image_number, image_url in enumerate(get_apod_image_list(token)):
        filename = f'./images/nasa_apod_{image_number}{get_extention_from_url(image_url)}'
        download_image(image_url, filename)
