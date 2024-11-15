import requests
import allure
from test_api_belov.endpoints.endpoint import Endpoint


class UpdateObjectPut(Endpoint):

    @allure.step('Update a object')
    def make_changes_in_object(self, object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(f'{self.url}/{object_id}', json=body, headers=headers)
        self.json = self.response.json()
        return self.response
