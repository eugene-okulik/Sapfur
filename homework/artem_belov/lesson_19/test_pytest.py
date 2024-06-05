import pytest
import requests


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


@pytest.mark.critical
@pytest.mark.parametrize('prices', [1849.99, '   ', '$%#%$@#&'])
def test_create_a_post(start_end_testing, start_end_test, prices):
    body = {
        "name": "Apple iphone 14 pro",
        "data": {
            "year": 2020,
            "prices": prices,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://api.restful-api.dev/objects', json=body, headers=headers)
    post_id = response.json()['id']

    assert response.status_code == 200, 'Status code is not 200'
    assert response.json()['data']['prices'] == prices, 'Price is not correct'

    requests.get(f'https://api.restful-api.dev/objects/{post_id}')


@pytest.mark.medium
def test_put_a_post(new_post_id, start_end_test):
    body = {
        "name": "Apple iphone 14 pro",
        "data": {
            "year": 2020,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'https://api.restful-api.dev/objects/{new_post_id}',
        json=body,
        headers=headers
    )
    response_data = response.json()
    print(f'Response data: {response_data}')
    assert response.status_code == 200, 'Status code is not 200'
    assert response_data['data'].get('color') == 'silver', 'Color was not updated correctly'


@pytest.mark.medium
def test_patch_a_post(new_post_id, start_end_test):
    body = {
        "name": "Apple iphone 14 pro (Updated Name)"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.patch(
        f'https://api.restful-api.dev/objects/{new_post_id}',
        json=body,
        headers=headers
    )
    response_data = response.json()
    print(f'Response data: {response_data}')
    assert response.status_code == 200, 'Status code is not 200'
    assert response_data['name'] == "Apple iphone 14 pro (Updated Name)", 'Name not updated'
    assert response_data['id'] == new_post_id, 'Id is not true'


@pytest.mark.critical
def test_delete_a_post(new_post_id, start_end_test):
    response = requests.delete(f'https://api.restful-api.dev/objects/{new_post_id}')
    print(f'Response data: {response}')
    assert response.status_code == 200, 'Status code is not 200'
