import pytest

from services.brewery_api_service import BreweryApiService


@pytest.fixture(scope="session")
def brewery_api():
    return BreweryApiService()

@pytest.mark.parametrize("brewery_id, brewery_name", [
    ('b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0', 'MadTree Brewing 2.0'),
])
def test_get_single_brewery(brewery_api, brewery_id, brewery_name):
    brewery = brewery_api.get_brewery_by_id(brewery_id)
    assert brewery.id == brewery_id, f"Expected {brewery_id}, bit got {brewery.id}"
    assert brewery.name == brewery_name, f"Expected {brewery_name}, bit got {brewery.name}"


@pytest.mark.parametrize("params", [
    {"by_city": "san diego"},
    {"by_name": "dog"},
    {"by_state": "california"},
    {"by_type": "micro"},
])
def test_list_breweries_with_filters(brewery_api, params):
    breweries = brewery_api.list_breweries(params)
    assert isinstance(breweries, list), f"Expected list, but got {type(breweries)}"
    assert len(breweries) > 0, f"Expected non-empty list, but got empty list for params {params}"
    key, value = list(params.items())[0]
    value = value.lower()

    for b in breweries:
        if key == "by_city":
            assert value in (b.city or "").lower(), \
                f"Expected brewery from city '{value}', but got '{b.city}'"
        elif key == "by_state":
            assert value in (b.state or "").lower(), \
                f"Expected brewery from state '{value}', but got '{b.state}'"
        elif key == "by_type":
            assert value in (b.brewery_type or "").lower(), \
                f"Expected brewery type '{value}', but got '{b.brewery_type}'"
        elif key == "by_name":
            assert value in (b.name or "").lower(), \
                f"Expected brewery name containing '{value}', but got '{b.name}'"


def test_search_breweries(brewery_api):
    query = "san diego"
    breweries = brewery_api.search_breweries(query, per_page=3)
    assert len(breweries) <= 3, f"Expected max 3 breweries, but got {len(breweries)}"
    assert len(breweries) > 0, "Expected at least one brewery in search results"

    for b in breweries:
        assert query in b.name.lower() or query in b.city.lower(), \
            f"Query '{query}' not found in name '{b.name}' or city '{b.city}'"


def test_autocomplete_breweries(brewery_api):
    query = "dog"
    suggestions = brewery_api.autocomplete(query)
    assert len(suggestions) > 0, f"Expected non-empty suggestions, but got empty list for query '{query}'"
    assert query in suggestions[0].name.lower(), \
        f"Query '{query}' not found in suggestion name '{suggestions[0].name}'"


@pytest.mark.parametrize("size", [25, 50])
def test_random_breweries_limit_positive(brewery_api, size):
    breweries = brewery_api.get_random_brewery(size)
    assert isinstance(breweries, list)
    assert len(breweries) == size


@pytest.mark.parametrize("size", [51, 100])
def test_random_breweries_limit_negative(brewery_api, size):
    with pytest.raises(ValueError) as exc:
        brewery_api.get_random_brewery(size)
    assert str(size) in str(exc.value)


@pytest.mark.parametrize("params", [
    {"by_city": "san diego"},
    {"by_name": "dog"},
    {"by_state": "california"},
    {"by_type": "micro"},
])
def test_get_metadata_brewery(brewery_api, params):
    meta = brewery_api.get_metadata(params)
    assert int(meta.total) > 0, f"Expected total > 0, but got {meta.total}"
    assert int(meta.page) == 1, f"Expected page 1, but got {meta.page}"
    assert int(meta.per_page) == 50, f"Expected per_page 50, but got {meta.per_page}"
