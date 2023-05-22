import requests
import os
from dotenv import load_dotenv
import telegram

def main():
    load_dotenv()
    token = os.environ['TLG_TOKEN']
    bot = telegram.Bot(token)
    return  bot.get_me()


if __name__ == '__main__':
    print(main())