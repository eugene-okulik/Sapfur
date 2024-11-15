import requests
import allure
from test_api_belov.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step('Delete an object')
    def delete_object(self, object_id):
        self.response = requests.delete(f'{self.url}/{object_id}')
