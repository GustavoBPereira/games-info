# Games info
## This project receive a game name and return informations about this game 

The price datas are getting from [steamDB](https://steamdb.info/)

The time datas are getting from [howlongtobeat](https://howlongtobeat.com/)

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
    "pk": 1,
    "created_at": "2020-03-26T00:40:41.071605Z",
    "updated_at": "2020-04-06T01:43:15.017910Z",
    "searched_game": "the witcher 3",
    "game_name": "The Witcher 3: Wild Hunt",
    "best_price": "R$ 23,99",
    "current_price": "R$ 23,99 at -70%",
    "time_information": [
        {
            "description": "Main Story",
            "content": "51 Hours"
        },
        {
            "description": "Main + Extra",
            "content": "102 Hours"
        },
        {
            "description": "Completionist",
            "content": "173 Hours"
        }
    ]
}
```

If this game is already searched before a new data will not be created,

the data registred with the same game_name(data returned from steamdb) will be overwritten
