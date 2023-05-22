import requests
import os
from dotenv import load_dotenv
import telegram

def main():
    load_dotenv()
    token = os.environ['TLG_TOKEN']
    chat_id = os.environ['TLG_CHAT_ID']
    bot = telegram.Bot(token)
    bot.send_message(chat_id=chat_id, text="publish text to Telegram channel.")
    return  bot.get_me()



if __name__ == '__main__':
    print(main())