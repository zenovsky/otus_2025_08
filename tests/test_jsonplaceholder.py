import pytest

from services.jsonplaceholder_api_service import JsonPlaceholderApiService


@pytest.fixture(scope="session")
def json_placeholder_api():
    return JsonPlaceholderApiService()


def test_post_has_expected_fields(json_placeholder_api):
    post = json_placeholder_api.get_post_by_id(1)
    assert post.userId == 1, f"Expected userId=1, but got {post.userId}"
    assert isinstance(post.title, str), f"Expected 'title' to be str, but got {type(post.title).__name__}"
    assert isinstance(post.body, str), f"Expected 'body' to be str, but got {type(post.body).__name__}"


@pytest.mark.parametrize("post_id", [1, 50, 100])
def test_get_post_by_id(json_placeholder_api, post_id):
    post = json_placeholder_api.get_post_by_id(post_id)
    assert post.id == post_id, f"Expected post.id={post_id}, but got {post.id}"


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_posts_by_user(json_placeholder_api, user_id):
    posts = json_placeholder_api.get_posts_by_user(user_id)
    for p in posts:
        assert p.userId == user_id, f"Expected userId={user_id}, but got {p.userId} for post.id={p.id}"


def test_create_post(json_placeholder_api):
    title, body, user_id = "foo", "bar", 1
    new_post = json_placeholder_api.create_post(title, body, user_id)

    assert new_post.title == title, f"Expected title='{title}', but got '{new_post.title}'"
    assert new_post.body == body, f"Expected body='{body}', but got '{new_post.body}'"
    assert new_post.userId == user_id, f"Expected userId={user_id}, but got {new_post.userId}"
    assert new_post.id is not None, "Expected new_post.id to be not None"


def test_update_post(json_placeholder_api):
    title, body, user_id, post_id = "updated", "new body", 1, 1
    updated = json_placeholder_api.update_post(post_id, title, body, user_id)

    assert updated.title == title, f"Expected title='{title}', but got '{updated.title}'"
    assert updated.body == body, f"Expected body='{body}', but got '{updated.body}'"
    assert updated.id == post_id, f"Expected post.id={post_id}, but got {updated.id}"


def test_delete_post(json_placeholder_api):
    response = json_placeholder_api.delete_post(1)
    assert response.status_code in (200, 204), f"Expected status 200 or 204, but got {response.status_code}"
