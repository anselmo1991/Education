from selene.support.conditions import be
from selene.support.shared import browser


@pytest.mark.parametrize("genre_name", ["Фэнтези", "Боевик"])
def go_to_genre(genre_name):
    browser.element('//a[text()="' + genre_name + '"]').should(be.visible).click()
