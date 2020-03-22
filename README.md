# Games info
## This project is an api that receive a game name and return informations about this game 

The price datas are getting from [steamDB](https://steamdb.info/)

## Usage

Basically make a post to /games-info/ with this parameters:

```
{
    'game_name': 'your_game_name'
}
```

The return will be a json with informations about this game:
```
{
    "pk": 1,
    "game_name": "The Witcher 3: Wild Hunt",
    "current_price": "R$ 79,99",
    "best_price": "R$ 23,99",
    "created_at": "2020-03-14T19:38:14.873178Z",
    "updated_at": "2020-03-14T22:42:45.296568Z",
    "searched_game_name": "the witcher 3"
}
```

If this game is already searched before a new data will not be created,

the data registred with the same game_name(data returned from steamdb) will be overwritten
