from multiprocessing import Pool
# from multiprocessing.dummy import Pool
import random
import sqlite3
import contextlib
from typing import Optional, List

from some_cookies.utils import news, db, browser
from some_cookies.core.settings import settings


news_list = []
# conn: Optional[sqlite3.Connection] = sqlite3.Connection(settings.database_path)


def return_random_urls() -> List[str]:
    result = [random.choice(news_list) for i in range(15)]
    return result


def run_for_profile(
        id: int,
        url: str
) -> None:

    with contextlib.closing(sqlite3.connect(settings.database_path)) as conn:

        # Get cookies (if exist)
        cookies = db.select_cookie(conn, id)[0]

        # Selenium session. Get new cookies.
        new_cookies = browser.get_data(
            url=url,
            driver_path=settings.driver_path,
            max_delay=settings.max_delay
        )

        # Write new cookies into database
        db.modify_data(
            conn=conn,
            id=id,
            cookie=new_cookies
        )


def run_the_pool() -> None:
    urls = return_random_urls()
    args = [(i, url) for i,url in zip(range(1, 16), urls)]
    with Pool(settings.max_processes) as p:
        p.starmap(run_for_profile, args)


def main():
    global news_list

    # Create DB and insert data
    db.create_db(settings.database_path)

    # Extract news references
    news_list = news.get_news(settings.news_url)

    # Run the Pool
    run_the_pool()


if __name__ == '__main__':
    main()
