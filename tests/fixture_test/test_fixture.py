import pytest


corporate_users = {
    "username": "corporate_user",
    "password": "corporate_password"
}

private_users = {
    "username": "private_user",
    "password": "private_password"
}


@pytest.fixture
def setup_user(request):
    user_type = request.node.get_closest_marker('user_type').args[0] if request.node.get_closest_marker(
        'user_type') else None

    if user_type == 'corporate':
        user_data = corporate_users
    elif user_type == 'private':
        user_data = private_users
    else:
        raise ValueError("Invalid user type. Please specify 'corporate' or 'private'.")

    return user_data


@pytest.mark.user_type('corporate')
def test_corporate_user(setup_user):
    expected_username = corporate_users['username']
    expected_password = corporate_users['password']

    actual_username = setup_user['username']
    actual_password = setup_user['password']

    assert actual_username == expected_username, f"Expected username: {expected_username}, but got: {actual_username}"
    assert actual_password == expected_password, f"Expected password: {expected_password}, but got: {actual_password}"


@pytest.mark.user_type('private')
def test_private_user(setup_user):
    expected_username = private_users['username']
    expected_password = private_users['password']

    actual_username = setup_user['username']
    actual_password = setup_user['password']

    assert actual_username == expected_username, f"Expected username: {expected_username}, but got: {actual_username}"
    assert actual_password == expected_password, f"Expected password: {expected_password}, but got: {actual_password}"
