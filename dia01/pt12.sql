--runs on sqlite
DROP TABLE IF EXISTS vals;

CREATE TABLE vals (
	l STRING
);

INSERT INTO vals VALUES (
	REPLACE(
		REPLACE(
			REPLACE(
				TRIM( 
					readfile('input.txt'),
					CHAR(10)
				),
				CHAR(13), 
				''),
			CHAR(10), 
			' '
			),
		'   ',
		' '
	)
);

DROP TABLE IF EXISTS lists;

CREATE TABLE lists (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	list INT NOT NULL
);

WITH RECURSIVE splitter(val, rest) AS (
	SELECT
		SUBSTR(l, 1, INSTR(l, ' ') - 1) AS val,
		SUBSTR(l || ' ', INSTR(l, ' ') + 1) AS rest
	FROM
		vals
	UNION
	SELECT
		SUBSTR(rest, 1, INSTR(rest, ' ') - 1) AS val,
		SUBSTR(rest, INSTR(rest, ' ') + 1) AS rest
	FROM
		splitter	
	WHERE
		INSTR(rest, ' ') > 0
)
INSERT INTO lists (list)
SELECT val FROM splitter;

DROP TABLE IF EXISTS list1;
DROP TABLE IF EXISTS list2;

CREATE TABLE list1 AS
SELECT 	list
FROM	lists
WHERE	ID % 2 <> 0;

CREATE TABLE list2 AS
SELECT	list 
FROM    lists
WHERE   ID % 2 = 0;

--pt1 answer
WITH Orderedlist1 AS (
	SELECT
		ROW_NUMBER() OVER(ORDER BY list) as ID,
		list
	FROM list1
	ORDER BY list
),
Orderedlist2 AS (
	SELECT
		ROW_NUMBER() OVER(ORDER BY list) as ID,
		list
	FROM list2
	ORDER BY list
)
SELECT
	SUM(
		ABS(
			L1.list - L2.list
		)
	)
FROM
	Orderedlist1 AS L1
INNER JOIN
	Orderedlist2 AS L2
ON
	L1.ID = L2.ID;

--pt2 answer

WITH Frequencylist2 AS (
        SELECT
                list,
                COUNT(list) AS freq
        FROM list2
        GROUP BY list
)
SELECT 
	SUM(
		L1.list * FL2.freq
	)
FROM 
	list1 AS L1
INNER JOIN
	Frequencylist2 AS FL2
ON 
	L1.list = FL2.list;
