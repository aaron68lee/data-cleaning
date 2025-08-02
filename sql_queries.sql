SELECT * FROM Menu WHERE event LIKE "%dinner%";

SELECT COUNT(*) FROM Menu WHERE event = "dinner";

SELECT COUNT(*) FROM Dish WHERE highest_price IS NULL;