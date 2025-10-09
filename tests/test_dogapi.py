import pytest

from models.dog_response_models import ErrorResponse
from services.dog_api_service import DogApiService


@pytest.fixture(scope="module")
def dog_api():
    return DogApiService()

@pytest.mark.parametrize("breed_name", ["hound", "husky", "pug"])
def test_list_all_breeds(dog_api, breed_name):
    response_data = dog_api.get_all_breeds()
    assert breed_name in response_data.message, f"Breed '{breed_name}' not found in the list of breeds"


@pytest.mark.parametrize("breed", ["hound", "husky", "pug"])
def test_get_breed_images(dog_api, breed):
    response_data = dog_api.get_breed_images(breed)
    for img_url in response_data.message:
        assert breed in str(img_url), f"{img_url} does not contain {breed}"


def test_request_non_existent_breed(dog_api):
    response_data = dog_api.get_breed_images("noexistbreed")
    assert isinstance(response_data, ErrorResponse)


@pytest.mark.parametrize("count, expected_count", [
    (51, 50),
    (101, 50),
])
def test_random_images_limit(dog_api, count, expected_count):
    response_data = dog_api.get_random_images(count)
    actual_count = len(response_data.message)
    assert actual_count == expected_count, \
        f"Expected {expected_count} images, but got {actual_count}"


@pytest.mark.parametrize("count", [1, 3, 50])
def test_get_multiple_random_images(dog_api, count):
    response_data = dog_api.get_random_images(count)
    assert len(response_data.message) == count
