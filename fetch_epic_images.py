import requests
import os
from dotenv import load_dotenv
from download_image import download_image


def get_epic_images(token):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {'api_key': token}
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    epics = []
    for epic in response.json():
        image = epic['image']
        year, month, day = epic['date'].split(' ')[0].split('-')
        epic_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image}.png'
        epics.append(epic_url)
    return epics


if __name__ == '__main__':
    os.makedirs("./images", exist_ok=True)
    load_dotenv()
    token = os.environ['NASA_TOKEN']

    for image_number, image_url in enumerate(get_epic_images(token)):
        image_url = f'{image_url}?api_key={token}'
        filename = f'./images/nasa_epic_{image_number}.png'
        download_image(image_url, filename)
