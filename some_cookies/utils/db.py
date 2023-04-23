import sqlite3
from sqlite3 import Error
from typing import Optional, Tuple, Union
import datetime
import contextlib
import os
from pathlib import Path

from some_cookies.utils.queries import update, select, insert, create
from some_cookies.core.settings import settings


def create_db(db: Union[str, os.PathLike]) -> None:

    if Path(db).is_file():
        return None

    conn = None
    try:
        conn = sqlite3.Connection(db)
        with contextlib.closing(conn.cursor()) as cur:
            insert_query = insert.insert_query
            create_query = create.create_query

            cur.execute(create_query)
            cur.execute(insert_query)

            conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def modify_data(
        conn: sqlite3.Connection,
        id: int,
        cookie: str,
        current_time: Optional[datetime.datetime] = None
) -> None:

    with contextlib.closing(conn.cursor()) as cur:

        query = update.update_query
        if current_time is None:
            current_time = datetime.datetime.now()

        cur.execute(query, (cookie, current_time, id))

        conn.commit()


def select_cookie(
        conn: sqlite3.Connection,
        id: int
) -> Tuple[Optional[str]]:

    with contextlib.closing(conn.cursor()) as cur:
        query = select.select_query
        query_result = cur.execute(query, (id,)).fetchone()

    return query_result


if __name__ == '__main__':
    print(create_db(settings.database_path))
    # with contextlib.closing(sqlite3.connect(settings.database_path)) as conn:
    #     print(select_cookie(conn, 1))
    #     modify_data(conn, 16, '123123', datetime.datetime.now())
