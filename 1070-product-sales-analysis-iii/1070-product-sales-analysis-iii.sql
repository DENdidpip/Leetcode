SELECT product_id, year AS first_year, quantity, price
FROM (
    SELECT 
        product_id,
        year,
        quantity,
        price,
        rank() OVER (
            PARTITION BY product_id 
            ORDER BY year
        ) AS t
    FROM Sales
) AS s
WHERE t = 1;