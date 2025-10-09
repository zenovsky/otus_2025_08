

from pydantic import BaseModel, ValidationError

from models.brewery_response_models import (
    AutocompleteListAdapter,
    Brewery,
    BreweryAutocomplete,
    BreweryListAdapter,
    Meta,
)
from services.api_client import ApiClient


class BreweryApiService:
    def __init__(self):
        self.base_url = "https://api.openbrewerydb.org/v1"
        self.client = ApiClient()


    def _validate_and_parse(self, response, model, expected_status=200):
        assert response.status_code == expected_status, \
            f"Expected {expected_status}, but got {response.status_code}."
        try:
            json_data = response.json()
            if isinstance(model, type) and issubclass(model, BaseModel):
                return model.model_validate(json_data)
            return model.validate_python(json_data)
        except ValidationError as e:
            raise AssertionError(f"Answer does not match the model:\n{e}")
        except ValueError:
            raise AssertionError("Failed to decode JSON from response.")


    def get_brewery_by_id(self, brewery_id: str) -> Brewery:
        url = f"{self.base_url}/breweries/{brewery_id}"
        response = self.client.get(url)
        return self._validate_and_parse(response, Brewery)


    def list_breweries(self, params: dict = None) -> list[Brewery]:
        url = f"{self.base_url}/breweries"
        response = self.client.get(url, params=params)
        return self._validate_and_parse(response, BreweryListAdapter)


    def get_random_brewery(self, size: int = 1) -> list[Brewery]:
        if size > 50:
            raise ValueError(f"Size must be <= 50, got {size}")
        url = f"{self.base_url}/breweries/random"
        response = self.client.get(url, params={"size": size})
        if response.status_code != 200:
            raise AssertionError(f"Expected 200, but got {response.status_code}")
        return self._validate_and_parse(response, BreweryListAdapter)


    def search_breweries(self, query: str, per_page: int = 5) -> list[Brewery]:
        url = f"{self.base_url}/breweries/search"
        params = {"query": query, "per_page": per_page}
        response = self.client.get(url, params=params)
        return self._validate_and_parse(response, BreweryListAdapter)


    def autocomplete(self, query: str) -> list[BreweryAutocomplete]:
        url = f"{self.base_url}/breweries/autocomplete"
        response = self.client.get(url, params={"query": query})
        return self._validate_and_parse(response, AutocompleteListAdapter)


    def get_metadata(self, params: dict = None) -> Meta:
        url = f"{self.base_url}/breweries/meta"
        response = self.client.get(url, params=params)
        return self._validate_and_parse(response, Meta)
