# Games info
## This project get some data about a searched game with crawler


The price data are getting from [steam api](http://store.steampowered.com/api/)

The time data are getting from [howlongtobeat](https://howlongtobeat.com/)

The app_ids data are getting from [steam api app list](http://api.steampowered.com/ISteamApps/GetAppList/v0001) 

## Usage

---
### Searching for games:
- Type a game to be searched

![search](./doc/img/search.png)

This will make a get to **/api/app_ids** api passing the searched string in q parameter.

The api will return a list of app_ids that will be used in /api/game in steam crawler part.

---

### Getting the search result:
- When you click in a game in the above select 

![result](./doc/img/result.png)

This will make a post to **/api/game** api passing the app_id and the language/currency, just like it:

```json
{
  "app_id": "292030",
  "currency": "br"
}
```

The api will a json with data about this game, just like it:

```json
{
    "id": 2,
    "app_id": 292030,
    "type": "game",
    "game_name": "The Witcher® 3: Wild Hunt",
    "short_description": "As war rages on throughout the Northern Realms, you take on the greatest contract of your life — tracking down the Child of Prophecy, a living weapon that can alter the shape of the world.",
    "supported_languages": "English<strong>*</strong>, French<strong>*</strong>, Italian, German<strong>*</strong>, Spanish - Spain, Arabic, Czech, Hungarian, Japanese<strong>*</strong>, Korean, Polish<strong>*</strong>, Portuguese - Brazil<strong>*</strong>, Russian<strong>*</strong>, Traditional Chinese, Turkish, Simplified Chinese<br><strong>*</strong>languages with full audio support",
    "metacritic_score": 93.0,
    "metacritic_url": "https://www.metacritic.com/game/pc/the-witcher-3-wild-hunt?ftag=MCD-06-10aaa1f",
    "recommendations": 422617,
    "comming_soon": false,
    "release_date": "May 18, 2015",
    "is_free": false,
    "discount_percent": 70.0,
    "initial_formatted": "$39.99",
    "final_formatted": "$11.99",
    "time_information": [
        {
            "description": "Main Story",
            "content": "51 Hours 30 Mins"
        },
        {
            "description": "Main + Extra",
            "content": "102 Hours"
        },
        {
            "description": "Completionist",
            "content": "173 Hours"
        }
    ],
    "header_image": "https://steamcdn-a.akamaihd.net/steam/apps/292030/header.jpg?t=1607418742",
    "background_image": "https://steamcdn-a.akamaihd.net/steam/apps/292030/ss_107600c1337accc09104f7a8aa7f275f23cad096.1920x1080.jpg?t=1607418742",
    "platforms": [
        {
            "platform": "windows",
            "supported": true
        },
        {
            "platform": "mac",
            "supported": false
        },
        {
            "platform": "linux",
            "supported": false
        }
    ],
    "genres": [
        "RPG"
    ]
}
```

## Setup

- create a .env file in the project root path
  - add SECRET_KEY=your_secret_key_here
  - add DEBUG=True or False 
- install requiremets with pip install -r requirements.txt
- run migrations with python manage.py migrate
- run the server with python manage.py runserver