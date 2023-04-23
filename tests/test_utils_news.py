from some_cookies.utils import news
from some_cookies.core.settings import settings


def test_get_news():
    assert news.get_news(settings.news_url)
