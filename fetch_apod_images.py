import requests
import os
from dotenv import load_dotenv
from download_image import download_image
from urllib.parse import urlparse


def get_extention_from_url(url):
    url_elements = urlparse(url)
    extention = os.path.splitext(url_elements.path)[1]
    return f'{extention}'


def get_apod_images(token, count=30):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': token, 'count': count}
    response = requests.get(url, params=params)
    response.raise_for_status()
    apod_urls = []
    for apod in response.json():
        apod_urls.append(apod['url'])
    return apod_urls


if __name__ == '__main__':
    os.makedirs("./images", exist_ok=True)
    load_dotenv()
    token = os.environ['NASA_TOKEN']

    for image_number, image_url in enumerate(get_apod_images(token)):
        filename = f'./images/nasa_apod_{image_number}{get_extention_from_url(image_url)}'
        download_image(image_url, filename)
