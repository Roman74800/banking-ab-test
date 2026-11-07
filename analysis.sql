-- PostgreSQL: primary metric, conversion per randomized user
SELECT variant,
       COUNT(DISTINCT user_id) AS users,
       SUM(completed) AS conversions,
       ROUND(SUM(completed)::numeric / NULLIF(COUNT(DISTINCT user_id),0),4) AS conversion_rate,
       ROUND(SUM(revenue_rub)::numeric / NULLIF(COUNT(DISTINCT user_id),0),2) AS arpu_rub
FROM experiment
GROUP BY variant;

-- Segment diagnostic (exploratory, not confirmatory)
SELECT channel, variant, COUNT(*) AS users, AVG(completed::numeric) AS conversion_rate
FROM experiment
GROUP BY channel, variant ORDER BY channel, variant;
