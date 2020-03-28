from django.test import TestCase, Client

from games_info.api.models import Game


class HomeTest(TestCase):

    # Removing game that will be tested
    try:
        game = Game.objects.get(game_name="Hellblade: Senua's Sacrifice")
        game.delete()
    except Game.DoesNotExist:
        pass

    c = Client()
    json_response = c.post('/games-api/', {'searched_game': 'hellblade'})

    def test_response_with_currect_name(self):
        self.assertEqual(self.json_response.json()['game_name'], "Hellblade: Senua's Sacrifice")

    def test_status_code_new_game_searched(self):
        self.assertEqual(self.json_response.status_code, 201)
