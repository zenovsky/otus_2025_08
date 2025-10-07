from services.api_client import ApiClient
from models.jsonplaceholder_response_model import Post

class JsonPlaceholderApiService:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"
        self.client = ApiClient()


    def _validate_response(self, response, expected_status=200):
        assert response.status_code == expected_status, \
            f"Expected {expected_status}, but got {response.status_code}"
        return response


    def get_posts(self):
        r = self.client.get(f"{self.base_url}/posts")
        return self._validate_response(r)


    def get_post_by_id(self, post_id: int):
        r = self.client.get(f"{self.base_url}/posts/{post_id}")
        self._validate_response(r)
        return Post(**r.json())


    def get_posts_by_user(self, user_id: int):
        r = self.client.get(f"{self.base_url}/posts", params={"userId": user_id})
        self._validate_response(r)
        return [Post(**p) for p in r.json()]


    def create_post(self, title: str, body: str, user_id: int):
        payload = {"title": title, "body": body, "userId": user_id}
        r = self.client.post(f"{self.base_url}/posts", json=payload)
        self._validate_response(r, expected_status=201)
        return Post(**r.json())


    def update_post(self, post_id: int, title: str, body: str, user_id: int):
        payload = {"id": post_id, "title": title, "body": body, "userId": user_id}
        r = self.client.put(f"{self.base_url}/posts/{post_id}", json=payload)
        self._validate_response(r)
        return Post(**r.json())


    def delete_post(self, post_id: int):
        r = self.client.delete(f"{self.base_url}/posts/{post_id}")
        self._validate_response(r, expected_status=200)
        return r