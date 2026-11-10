SELECT id, visit_date, people
FROM (
    SELECT *,
        COUNT(*) OVER (PARTITION BY grp) AS cnt
    FROM (
        SELECT *,
            id - ROW_NUMBER() OVER (ORDER BY id) AS grp
        FROM Stadium
        WHERE people >= 100
    ) AS tmp
) AS tmp2
WHERE cnt >= 3
ORDER BY visit_date;