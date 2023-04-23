import requests

from typing import List
import re


def reference_parser(page_content: str) -> List[str]:
    pattern = re.compile('href="[.](/articles/.*?)"')
    references = re.findall(pattern, page_content)
    return references


def get_news(url: str) -> List[str]:
    response = requests.get(url)
    references = reference_parser(response.content.decode())
    news_urls = [url + reference for reference in references]
    return news_urls
