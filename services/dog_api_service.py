from pydantic import ValidationError

from models.dog_response_models import (
    ErrorResponse,
    ImagesResponse,
    ListAllBreedsResponse,
    RandomImageResponse,
)
from services.api_client import ApiClient


class DogApiService:
    def __init__(self):
        self.base_url = "https://dog.ceo/api"
        self.client = ApiClient()


    def _validate_response(self, response, model, expected_status=200):
        assert response.status_code == expected_status, \
            f"Expected {expected_status}, but got {response.status_code}"
        try:
            parsed_data = model.model_validate(response.json())
            return parsed_data
        except ValidationError as e:
            raise AssertionError(f"Answer does not match the model {model.__name__}:\n{e}")
        except ValueError:
            raise AssertionError("Failed to decode JSON from response.")


    def get_all_breeds(self) -> ListAllBreedsResponse:
        url = f"{self.base_url}/breeds/list/all"
        response = self.client.get(url)
        return self._validate_response(response, ListAllBreedsResponse)


    def get_random_images(self, count: int = 1) -> ImagesResponse:
        if count == 1:
            url = f"{self.base_url}/breeds/image/random"
            response = self.client.get(url)
            validated_response = self._validate_response(response, RandomImageResponse)
            validated_response.message = [validated_response.message]
            return ImagesResponse.model_validate(validated_response.model_dump())

        url = f"{self.base_url}/breeds/image/random/{count}"
        response = self.client.get(url)
        return self._validate_response(response, ImagesResponse)


    def get_breed_images(self, breed: str) -> ImagesResponse | ErrorResponse:
        url = f"{self.base_url}/breed/{breed}/images"
        response = self.client.get(url)

        if response.status_code == 200:
            return self._validate_response(response, ImagesResponse)
        elif response.status_code == 404:
            return self._validate_response(response, ErrorResponse, expected_status=404)
        else:
            raise AssertionError(
            f"Unexpected status code {response.status_code}")
