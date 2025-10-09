
from pydantic import BaseModel, HttpUrl, TypeAdapter


class Brewery(BaseModel):
    id: str
    name: str
    brewery_type: str
    address_1: str | None = None
    address_2: str | None = None
    address_3: str | None = None
    city: str
    state_province: str | None = None
    state: str | None = None
    postal_code: str | None = None
    country: str
    longitude: str | float | None = None
    latitude: str | float | None = None
    phone: str | None = None
    website_url: HttpUrl | str | None = None
    street: str | None = None


class BreweryAutocomplete(BaseModel):
    id: str
    name: str


class Meta(BaseModel):
    total: str | int | None = None
    page: str | int | None = None
    per_page: str | int | None = None
    by_state: dict[str, int] | None = None
    by_type: dict[str, int] | None = None



BreweryListAdapter = TypeAdapter(list[Brewery])
AutocompleteListAdapter = TypeAdapter(list[BreweryAutocomplete])
