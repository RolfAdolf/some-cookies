import pytest

import tempfile
from pathlib import Path

from some_cookies.utils import db


@pytest.fixture()
def create_dir():
    with tempfile.TemporaryDirectory() as test_folder:
        yield test_folder


def test_create_db(create_dir):

    db_path = Path(create_dir) / 'test_db.db'
    db.create_db(db_path)
    assert db_path.is_file()
