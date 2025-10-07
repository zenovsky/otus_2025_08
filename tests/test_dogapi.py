import pytest

from models.dog_response_models import ErrorResponse
from services.dog_api_service import DogApiService


@pytest.fixture(scope="session")
def dog_api():
    return DogApiService()


def test_list_all_breeds_contains_hound(dog_api):
    response_data = dog_api.get_all_breeds()
    assert "hound" in response_data.message, "Breed 'hound' not found in the list"


def test_get_husky_images(dog_api):
    response_data = dog_api.get_breed_images("husky")
    for img_url in response_data.message:
        assert "husky" in str(img_url), f"{img_url} does not contain 'husky'"


def test_request_non_existent_breed(dog_api):
    expected_code = 404
    response_data = dog_api.get_breed_images("noexistbreed")
    assert isinstance(response_data, ErrorResponse)
    assert response_data.code == expected_code


def test_random_images_limit(dog_api):
    response_data = dog_api.get_random_images(51)
    actual_count = len(response_data.message)
    expected_count = 50
    assert actual_count == expected_count, \
        f"Expected {expected_count} images, but got {actual_count}"


@pytest.mark.parametrize("count", [1, 3, 50])
def test_get_multiple_random_images(dog_api, count):
    response_data = dog_api.get_random_images(count)
    assert len(response_data.message) == count
