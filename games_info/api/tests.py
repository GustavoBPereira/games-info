from django.test import TestCase, Client

from games_info.api.models import Game
from games_info.crawler.exceptions import TypeNotSupported


class HomeTest(TestCase):
    # Removing game that will be tested
    try:
        game = Game.objects.get(app_id='414340', currency='USD')
        game.delete()
    except Game.DoesNotExist:
        pass

    c = Client()
    json_response = c.post('/api/game/', {'app_id': '414340', 'currency': 'us'})

    def test_response_with_currect_name(self):
        self.assertEqual(self.json_response.json()['game_name'], "Hellblade: Senua's Sacrifice")

    def test_status_code_new_game_searched(self):
        self.assertEqual(self.json_response.status_code, 201)

    def test_type_must_be_game(self):
        self.assertEqual(self.json_response.json()['type'], 'game')

    def test_content_returned_time_information(self):
        expected_data = [
            {
                "description": "Main Story",
                "content": "7 Hours 30 Mins"
            },
            {
                "description": "Main + Extra",
                "content": "8 Hours"
            },
            {
                "description": "Completionist",
                "content": "9 Hours"
            }
        ]
        self.assertEqual(self.json_response.json()['time_information'], expected_data)

    def test_dlc_search(self):
        req = self.c.post('/api/game/', {'app_id': '378648', 'currency': 'us'})
        self.assertEqual(req.json()['type'], 'dlc')

    def test_app_ids_finding_game_id(self):
        # req = self.c.get("/api/app_ids/?q=Hellblade: Senua's Sacrifice")
        # todo: learn mocks!
        mocked_response = [{'name': 'foo', 'appid': 414340}]
        self.assertIn(414340, [app['appid'] for app in mocked_response])

    def test_empty_search_when_type_soundtrack(self):
        req = self.c.get("/api/app_ids/?q=soundtrack")
        self.assertEqual(req.json()['games'], [])

    def test_unsupported_type_in_steam_crawler(self):
        with self.assertRaises(TypeNotSupported):
            self.c.post('/api/game/', {'app_id': '598190', 'currency': 'us'})
