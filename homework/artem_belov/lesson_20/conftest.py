import allure
import requests
import pytest


@pytest.fixture()
def new_post_id():
    body = {
        "name": "Apple iphone 14 pro",
        "data": {
            "year": 2020,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers
    )
    post_id = response.json()['id']
    yield post_id
    requests.delete(f'https://api.restful-api.dev/objects/{post_id}')


@pytest.fixture(scope='function')
def start_end_test():
    print('\nbefore test')
    yield
    print('\nafter test')


@pytest.fixture(scope='session')
def start_end_testing():
    print('\nStart testing')
    yield
    print('\nTesting completed')
