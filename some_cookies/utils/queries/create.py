create_query = """
CREATE TABLE main."Cookie Profile"(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    created_at TEXT NOT NULL,
    cookie TEXT,
    last_launch_at TEXT,
    count_launches INTEGER DEFAULT 0
);
"""