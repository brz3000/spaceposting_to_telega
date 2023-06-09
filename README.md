# Скрипт предназначен постинга фото в телеграм. 

 Скрипт предназначен для постинга фото с указанной директории в телеграм.
Скачивание фото с сайта NASA и spacex реализовано в отдельных скриптах fetch_apod_images.py, 
fetch_epic_images.py и fetch_spacex_images.py.
Используется [API NASA](https://api.nasa.gov/), и API [spaceX](https://github.com/r-spacex/SpaceX-API)

## Описание
 Скрипт предназначен для скачивания фото с сайта nasa и постинга в телеграм. 


## Требования
Для работы должен быть установлен python3. А также необходимо установить библиотеки requests, python-dotenv,
python-telegram-bot==13.15, которые описаны в файле requirements.txt

## Установка
Чтобы установить python3 скачайте и ознакомьтесь с инструкцией по установке на сайте[python.org](https://www.python.org/downoloads)

Библиотеки устанавливаются командой:
```bash
    pip install -r requirements.txt
```

## Использование
Для использования скрипта необходимо его запустить:
```bash
python bot.py
```
Возможно изменить время через которое бот будет постить сообщения.
Задаётся в минутах через аргумент --timeout.

## Пример использования скрипта

``` bash
python bot.py --timeout 1
```
в данном примере фотографии будут отправляться каждую минуту

Пример запуска скрипта для скачивания картинок с сайта space X. Если не указывать аргумент,
то скачиваются фотографии с последнего запуска (если фотографии присутствуют). 
Также можно указать с какого запуска скачивать фотографии:
через аргумент -l. В примере ниже скачиваются фотографии с запуска с id = 5eb87d47ffd86e000604b38a
``` bash
python fetch_spacex_images.py -l 5eb87d47ffd86e000604b38a
```

Пример запуска скрипта для скачивания картинок Astronomy Picture of the Day с сайта [NASA.gov](https://api.nasa.gov/).
``` bash
python fetch_apod_images.py
```

Пример запуска скрипта для скачивания картинок Earth Polychromatic Imaging Camera (EPIC) с сайта [NASA.gov](https://api.nasa.gov/).
``` bash
python fetch_epic_images.py
```

## Настройки
Необходимо чтобы в дирректории проекта был файл .env, в котором содержаться переменные окружения:
* TLG_TOKEN - токен телеграм бота, узнать можно у @BotFather
* TLG_CHAT_ID - id чата с ботом. Узнать можно написав боту @userinfobot
* NASA_TOKEN - Токен [NASA APIs](https://api.nasa.gov/). Если у вас нет токена nasa, можно использовать api_key='DEMO_KEY'.
* DELAY - значение по умолчанию для таймаута постинга, задаётся в минутах, возможно задать как аргумент бота.


