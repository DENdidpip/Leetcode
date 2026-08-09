SELECT sp.name
FROM SalesPerson sp
WHERE sp.sales_id NOT IN (
    SELECT o.sales_id
    FROM Orders o
    JOIN Company c ON c.com_id = o.com_id
    WHERE c.name = 'RED'
);