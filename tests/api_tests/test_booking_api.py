import requests
import pytest
import allure
from hamcrest import assert_that, equal_to, has_item

BASE_URL = "https://restful-booker.herokuapp.com"

USERNAME = "admin"
PASSWORD = "password123"
BOOKING_DATA = {
    "firstname": "John",
    "lastname": "Doe",
    "bookingdates": {
        "checkin": "2024-04-17",
        "checkout": "2024-04-18"
    },
    "additionalneeds": "Breakfast"
}


@pytest.fixture
def auth_token_():
    response = requests.post(f"{BASE_URL}/auth", json={"username": USERNAME, "password": PASSWORD})
    token = response.json()["token"]
    return token


@pytest.fixture
def headers_(auth_token_):
    return {"Content-Type": "application/json", "Accept": "application/json", "Cookie": f"token={auth_token_}"}


@allure.step("Login with token")
def test_login():
    response = requests.post(f"{BASE_URL}/auth", json={"username": USERNAME, "password": PASSWORD})
    assert_that(response.status_code, equal_to(200))


@allure.step("Create booking")
def test_create_booking(headers_):
    response = requests.post(f"{BASE_URL}/booking", json=BOOKING_DATA, headers=headers_)
    assert_that(response.status_code, equal_to(200))


@allure.step("Check that booking was created")
def test_check_booking_creation(headers_):
    response = requests.get(f"{BASE_URL}/booking", headers=headers_)
    assert_that(response.status_code, equal_to(200))
    booking_ids = [booking["bookingid"] for booking in response.json()]
    assert_that(booking_ids, has_item(BOOKING_DATA["firstname"]))
