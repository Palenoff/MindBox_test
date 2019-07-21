SELECT *
FROM Products P LEFT OUTER JOIN (
	SELECT *
	FROM Products_Categories PC LEFT OUTER JOIN Categories C ON PC.id_Category = C.id
	) PC
   ON P.id = PC.id_Product

Исхожу из того, что связи между продуктами и категориями хранятся в отдельной таблице Products_has_Categories, в которой есть поля
Products_id и Categories_id.
Схему БД смотри в файле DB_scheme.pdf