from some_cookies.utils import browser
from some_cookies.core.settings import settings


def test_get_data():
    result = browser.get_data(
        settings.news_url,
        settings.driver_path,
        1
    )
    assert result

    exception_url = 'https://instagram.com'
    result = browser.get_data(
        exception_url,
        settings.driver_path,
        1
    )
    assert result is None
