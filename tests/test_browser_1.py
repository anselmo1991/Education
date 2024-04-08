import pytest


def test_browser(open_browser):
    # Получаем браузер из фикстуры
    open_browser.get("https://www.google.com")

