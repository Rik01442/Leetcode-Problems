/* Write your T-SQL query statement below */

WITH Dups AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn
  FROM Person
)
DELETE FROM Dups WHERE rn > 1;
