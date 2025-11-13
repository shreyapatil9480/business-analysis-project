-- Stakeholder summary metrics for D08
SELECT
  COUNT(*) AS total_records,
  AVG(CAST(satisfied AS FLOAT)) AS satisfied_rate
FROM client_satisfaction;

SELECT *
FROM client_satisfaction
ORDER BY 1
LIMIT 10;
