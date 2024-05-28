import requests


def new_post():
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
    return response.json()['id']


def clear(post_id):
    requests.delete(f'https://api.restful-api.dev/objects/{post_id}')


def put_a_post():
    post_id = new_post()
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
        f'https://api.restful-api.dev/objects/{post_id}',
        json=body,
        headers=headers
    )
    response_data = response.json()
    print(f'Response data: {response_data}')
    assert response_data["data"].get("color") == "silver", "Color was not updated correctly"
    clear(post_id)


def patch_a_post():
    post_id = new_post()
    body = {
        "name": "Apple iphone 14 pro (Updated Name)"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{post_id}',
        json=body,
        headers=headers
    ).json()
    print(response)
    clear(post_id)


def delete_a_post():
    post_id = new_post()
    response = requests.delete(f'https://api.restful-api.dev/objects/{post_id}')
    print(response.json())
    print(response.status_code)


new_post()
put_a_post()
patch_a_post()
delete_a_post()
