# Games info
## This project is an api that receive a game name and return informations about this game 

The price datas are getting from [steamDB](https://steamdb.info/)

## Usage

Basically make a post to /games-info/ with this parameters:

```
{
    'searched_game': 'the witcher 3'
}
```

The return will be a json with informations about this game:
```
{
    'created_at': '2020-03-24T01:22:36.759145Z',
    'updated_at': '2020-03-24T01:22:36.759204Z',
    'searched_game': 'the witcher 3',
    'game_name': 'The Witcher 3: Wild Hunt',
    'best_price': 'R$ 23,99',
    'current_price': 'R$ 23,99 at -70%'
}
```

If this game is already searched before a new data will not be created,

the data registred with the same game_name(data returned from steamdb) will be overwritten
