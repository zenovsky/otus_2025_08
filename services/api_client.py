import requests
from requests import Response


class ApiClient:
    def __init__(self):
        self.session = requests.Session()


    def get(self, url: str, params: dict = None) -> Response:
        try:
            response = self.session.get(url, params=params)
            return response
        except requests.exceptions.RequestException:
            raise

    def post(self, url, json=None):
        return requests.post(url, json=json)

    def put(self, url, json=None):
        return requests.put(url, json=json)

    def delete(self, url):
        return requests.delete(url)
