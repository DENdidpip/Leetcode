SELECT ROUND(
    COUNT(*) / (SELECT COUNT(DISTINCT player_id) FROM Activity),
    2
) AS fraction
FROM (
    SELECT player_id
    FROM Activity
    GROUP BY player_id
    HAVING DATE_ADD(MIN(event_date), INTERVAL 1 DAY) IN (
        SELECT event_date
        FROM Activity a2
        WHERE a2.player_id = Activity.player_id
    )
) AS t;