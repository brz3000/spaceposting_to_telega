import requests
import os
from pathlib import Path
from urllib.parse import urlparse
from urllib.parse import unquote
from dotenv import load_dotenv


def download_image(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def get_images_list_from_spacex(launch=''):
    url_template = 'https://api.spacexdata.com/v5/launches/{}'
    if not launch:
        launch = 'latest'
    url = url_template.format(launch)
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def get_filename_from_url(url):
    url_elements = urlparse(url)
    extention = os.path.splitext(url_elements.path)[1]
    filename = unquote(os.path.splitext(os.path.split(url_elements.path)[1])[0])
    return f'{filename}{extention}'


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


def get_epic_image_list(token):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {'api_key': token}
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    epic_list = []
    for epic in response.json():
        image = epic['image']
        year, month, day = epic['date'].split(' ')[0].split('-')
        epic_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image}.png'
        epic_list.append(epic_url)
    return epic_list


if __name__ == '__main__':
    Path("./images").mkdir(parents=True, exist_ok=True)
    if not os.path.exists("./images"):
        os.makedirs("./images")
    load_dotenv()
    token = os.environ['NASA_TOKEN']

    for image_number, image_url in enumerate(get_images_list_from_spacex('5eb87d47ffd86e000604b38a')):
        filename = f'./images/spacex{image_number}.jpeg'
        download_image(image_url, filename)
    for image_number, image_url in enumerate(get_apod_image_list(token)):
        filename = f'./images/nasa_apod_{image_number}{get_extention_from_url(image_url)}'
        download_image(image_url, filename)
    for image_number, image_url in enumerate(get_epic_image_list(token)):
        image_url = f'{image_url}?api_key={token}'
        filename = f'./images/nasa_epic_{image_number}.png'
        download_image(image_url, filename)
