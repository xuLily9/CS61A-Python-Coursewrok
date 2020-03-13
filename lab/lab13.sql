.read su19data.sql

CREATE TABLE obedience AS
  SELECT seven, instructor FROM students;

CREATE TABLE smallest_int AS
  SELECT time,smallest FROM students GROUPBY WHERE smallest > 2 ORDER BY smallest LIMIT 20;

CREATE TABLE matchmaker AS
  SELECT first.pet, first.song, first.color, second.color
  from students as first, students as second
  where first.pet = second.pet AND first.song = second.song AND first.time < second.time;

CREATE TABLE smallest_int_having AS
SELECT time, smallest FROM students GROUP BY smallest HAVING COUNT(*) = 1 ORDER BY smallest;
