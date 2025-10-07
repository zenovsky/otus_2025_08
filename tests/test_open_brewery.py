import pytest

from services.brewery_api_service import BreweryApiService


@pytest.fixture(scope="session")
def brewery_api():
    return BreweryApiService()


def test_get_single_brewery(brewery_api):
    brewery_id = "b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0"
    brewery_name = "MadTree Brewing 2.0"
    brewery = brewery_api.get_brewery_by_id(brewery_id)
    assert brewery.id == brewery_id, f"Expected {brewery_id}, bit got {brewery.id}"
    assert brewery.name == brewery_name, f"Expected {brewery_name}, bit got {brewery.name}"


@pytest.mark.parametrize("params", [
    {"by_city": "san_diego"},
    {"by_name": "dog"},
    {"by_state": "california"},
    {"by_type": "micro"},
])
def test_list_breweries_with_filters(brewery_api, params):
    breweries = brewery_api.list_breweries(params)
    assert isinstance(breweries, list), f"Expected list, but got {type(breweries)}"
    assert len(breweries) > 0, f"Expected non-empty list, but got empty list for params {params}"


def test_search_breweries(brewery_api):
    query = "san diego"
    breweries = brewery_api.search_breweries(query, per_page=3)
    assert len(breweries) <= 3, f"Expected max 3 breweries, but got {len(breweries)}"
    assert query in breweries[0].name.lower() or query in breweries[0].city.lower(), \
        f"Query '{query}' not found in name '{breweries[0].name}' or city '{breweries[0].city}'"


def test_autocomplete_breweries(brewery_api):
    query = "dog"
    suggestions = brewery_api.autocomplete(query)
    assert len(suggestions) > 0, f"Expected non-empty suggestions, but got empty list for query '{query}'"
    assert query in suggestions[0].name.lower(), \
        f"Query '{query}' not found in suggestion name '{suggestions[0].name}'"

@pytest.mark.parametrize("size", [
    (1),
    (50),
])
def test_random_breweries_limit_positive(brewery_api, size):
    breweries = brewery_api.get_random_brewery(size)
    assert len(breweries) == size, f"Expected {size} breweries, but got {len(breweries)}"

def test_get_metadata_brewery(brewery_api):
    params = {"by_city": "san_diego"}
    meta = brewery_api.get_metadata(params)
    assert int(meta.total) > 0, f"Expected total > 0, but got {meta.total}"
    assert int(meta.page) == 1, f"Expected page 1, but got {meta.page}"
    assert int(meta.per_page) == 50, f"Expected per_page 50, but got {meta.per_page}"
