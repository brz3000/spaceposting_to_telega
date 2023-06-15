import requests
import os
import argparse
from download_image import download_image


def get_images_from_spacex(launch='latest'):
    url_template = 'https://api.spacexdata.com/v5/launches/{}'
    url = url_template.format(launch)
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


if __name__ == '__main__':
    os.makedirs("./images", exist_ok=True)
    parser = argparse.ArgumentParser(description='''<Script for download launch images from SpaceX REST API.
                                                 By default downloading image from latest launch.
                                                 You may use -l argument for ask how  launch  do you need. Example
                                                 "python fetch_spacex_images.py -l 5eb87d47ffd86e000604b38a" >''')
    parser.add_argument("-l", default='latest', type=str, help="Input id launch")
    args = parser.parse_args()

    for image_number, image_url in enumerate(get_images_from_spacex(args.l)):
        file_path = f'./images/spacex{image_number}.jpeg'
        download_image(image_url, file_path)
