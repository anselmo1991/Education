import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def open_browser():
    """
    Open browser
    """
    # Инициализация драйвера
    driver = webdriver.Firefox()
    yield driver
    # Здесь не будет закрытия браузера после завершения теста
