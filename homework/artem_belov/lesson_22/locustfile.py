from locust import task, HttpUser
import random


class Booker(HttpUser):
    token = None

    def on_start(self):
        response = self.client.post(
            '/auth',
            json={"username": "admin", "password": "password123"}
        )
        self.token = response.json()['token']

    @task(3)
    def get_all_books(self):
        self.client.get(
            '/booking',
            headers={'Authorization': self.token}
        )

    @task(1)
    def get_one_book(self):
        self.client.get(
            f'/booking/{random.choice([128, 224, 140, 282])}',
            headers={'Authorization': self.token}
        )
