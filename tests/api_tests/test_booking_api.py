import requests
import pytest
import allure

BASE_URL = "https://restful-booker.herokuapp.com"

USERNAME = "admin"
PASSWORD = "password"
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
def auth_token():
    response = requests.post(f"{BASE_URL}/auth", json={"username": USERNAME, "password": PASSWORD})
    token = response.json()["token"]
    return token


@pytest.fixture
def headers_(auth_token_):
    return {"Content-Type": "application/json", "Accept": "application/json", "Cookie": f"token={auth_token_}"}


@allure.step("Login with token")
def test_login():
    response = requests.post(f"{BASE_URL}/auth", json={"username": USERNAME, "password": PASSWORD})
    assert response.status_code == 200


@allure.step("Create booking")
def test_create_booking(headers_):
    response = requests.post(f"{BASE_URL}/booking", json=BOOKING_DATA, headers=headers_)
    assert response.status_code == 200


@allure.step("Check that booking was created")
def test_check_booking_creation(headers_):
    response = requests.get(f"{BASE_URL}/booking", headers=headers_)
    assert response.status_code == 200
    booking_id = response.json()[-1]["bookingid"]
    assert booking_id is not None
