SELECT *
FROM Products P LEFT OUTER JOIN (
	SELECT *
	FROM Products_Categories PC LEFT OUTER JOIN Categories C ON PC.id_Category = C.id
	) PC
   ON P.id = PC.id_Product

������ �� ����, ��� ����� ����� ���������� � ����������� �������� � ��������� ������� Products_has_Categories, � ������� ���� ����
Products_id � Categories_id.
����� �� ������ � ����� DB_scheme.pdf