from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def index(self):
        self.client.get('/')

    @task(5)
    def app_id_search(self):
        self.client.get('/api/app_ids/?q=hellblade')

    @task(5)
    def search_game(self):
        self.client.post('/api/game/', data={'app_id': '414340'})
