from tests.selectors import SELECTOR_SORT_BY_COMMENTS, SELECTOR_COUNTERS, SELECTOR_BOOK_INFO
from selene.support.shared import browser

comments_filter = browser.element(SELECTOR_SORT_BY_COMMENTS)
all_counters = browser.all(SELECTOR_COUNTERS)
books = browser.all(SELECTOR_BOOK_INFO)