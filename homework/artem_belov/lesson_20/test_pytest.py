import pytest
import requests
import allure


@allure.epic('API')
@allure.feature('CRUD operations')
@allure.story('POST')
@allure.title('Create object')
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

    with allure.step('Check status code is 200'):
        assert response.status_code == 200, 'Status code is not 200'

    with allure.step(f'Check that new object price is {prices}'):
        assert response.json()['data']['prices'] == prices, 'Price is not correct'

    requests.get(f'https://api.restful-api.dev/objects/{post_id}')


@allure.epic('API')
@allure.feature('CRUD operations')
@allure.story('PUT')
@allure.title('Complete object update')
@pytest.mark.medium
def test_put_a_post(new_post_id, start_end_test):
    body = {
        "name": "Apple iphone 14 pro",
        "data": {
            "year": 2020,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "red"
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
    with allure.step('Check status code is 200'):
        assert response.status_code == 200, 'Status code is not 200'

    with allure.step('Field added'):
        assert response_data['data'].get('color') == 'red', 'Color was not updated correctly'


@allure.epic('API')
@allure.feature('CRUD operations')
@allure.story('PATCH')
@allure.title('Partial object update')
@pytest.mark.medium
def test_patch_a_post(new_post_id, start_end_test):
    body = {"name": "Apple iphone 14 pro (Updated Name)"}
    headers = {'Content-Type': 'application/json'}

    response = requests.patch(
        f'https://api.restful-api.dev/objects/{new_post_id}',
        json=body,
        headers=headers
    )
    response_data = response.json()
    print(f'Response data: {response_data}')
    with allure.step('Check status code is 200'):
        assert response.status_code == 200, 'Status code is not 200'

    with allure.step('Checking that the field has changed'):
        assert response_data['name'] == "Apple iphone 14 pro (Updated Name)", 'Name not updated'

    with allure.step(f'Check that object id is {new_post_id}'):
        assert response.json()['id'] == new_post_id, 'Id is not correct'


@allure.epic('API')
@allure.feature('CRUD operations')
@allure.story('DELETE')
@allure.title('Delete an object')
@pytest.mark.critical
def test_delete_a_post(new_post_id, start_end_test):
    with allure.step(f'Run delete request for delete and object with id {new_post_id}'):
        response = requests.delete(f'https://api.restful-api.dev/objects/{new_post_id}')

    with allure.step('Check status code is 200'):
        assert response.status_code == 200, 'Status code is not 200'
    print(f'Response data: {response}')
