import pytest
import allure

TEST_DATA_CREATE = [
    {
        "name": "Apple MacBook Pro 16",
        "data": {"year": 2019, "price": 1999.99, "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}
    },
    {
        "name": "Apple MacBook Pro 16",
        "data": {"year": 2029, "price": 5341, "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}
    }
]

TEST_DATA_UPDATE_PUT = [
    {
        "name": "Apple MacBook Air M1",
        "data": {"year": 2019, "price": 1000, "CPU model": "M1", "Hard disk size": "256 GB", "color": "black"}
    },
    {
        "name": "Apple MacBook Air 2019",
        "data": {"year": 2019, "price": 1400, "CPU model": "Intel Core i9", "Hard disk size": "512 GB"}
    }
]

TEST_DATA_UPDATE_PATCH = [
    {"name": "Apple iphone 14 pro (Updated Name)"}, {"name": "Apple MacBook Air 2019 (Updated Name)"}
]


@allure.epic('API')
@allure.feature('CRUD operations')
@allure.story('POST')
@allure.title('Create an object')
@pytest.mark.critical
@pytest.mark.parametrize('data', TEST_DATA_CREATE)
def test_create_an_object(create_object_endpoint, start_end_testing, start_end_test, data):
    create_object_endpoint.new_object(body=data)
    create_object_endpoint.check_that_status_is_200()
    create_object_endpoint.check_response_price_is_correct(data['data']['price'])


@allure.epic('API')
@allure.feature('CRUD operations')
@allure.story('PUT')
@allure.title('Complete object update')
@pytest.mark.medium
@pytest.mark.parametrize('data', TEST_DATA_UPDATE_PUT)
def test_put_an_object(update_object_endpoint_put, new_post_id, start_end_test, data):
    update_object_endpoint_put.make_changes_in_object(new_post_id, body=data)
    update_object_endpoint_put.check_that_status_is_200()
    update_object_endpoint_put.check_response_price_is_correct(data['data']['price'])
    update_object_endpoint_put.check_response_id_is_correct(new_post_id)


@allure.epic('API')
@allure.feature('CRUD operations')
@allure.story('PATCH')
@allure.title('Partial object update')
@pytest.mark.parametrize('data', TEST_DATA_UPDATE_PATCH)
def test_patch_an_object(update_object_endpoint_patch, new_post_id, start_end_test, data):
    update_object_endpoint_patch.make_partial_changes_in_object(new_post_id, body=data)
    update_object_endpoint_patch.check_that_status_is_200()
    update_object_endpoint_patch.check_response_name_is_correct(data['name'])
    update_object_endpoint_patch.check_response_id_is_correct(new_post_id)


@allure.epic('API')
@allure.feature('CRUD operations')
@allure.story('DELETE')
@allure.title('Delete an object')
def test_delete_an_object(delete_object_endpoint, get_object_endpoint, new_post_id, start_end_test):
    delete_object_endpoint.delete_object(new_post_id)
    delete_object_endpoint.check_that_status_is_200()
    get_object_endpoint.get_object(new_post_id)
    get_object_endpoint.check_that_object_was_deleted()
    get_object_endpoint.check_that_status_is_404()


