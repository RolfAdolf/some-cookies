update_query = """
UPDATE main."Cookie Profile"
SET cookie = ?,
    last_launch_at = ?,
    count_launches = count_launches + 1
WHERE
    id = ?;
"""