
-- TYPE YOUR SQL QUERY BELOW

-- PART 1: Create a SQL query that maps out the daily average users
-- before and after the feature change.
-- Kanban Board release date: 2018-06-02

SELECT
    DATE(login_timestamp, 'unixepoch') AS login_date,
    COUNT(DISTINCT user_id) AS daily_active_users,
    CASE
        WHEN DATE(login_timestamp, 'unixepoch') < '2018-06-02'
        THEN 'Before Release'
        ELSE 'After Release'
    END AS release_period
FROM login_history
GROUP BY DATE(login_timestamp, 'unixepoch')
ORDER BY login_date;


-- PART 2: Create a SQL query that indicates the number
-- of status changes by card

SELECT
    cardID AS card_id,
    COUNT(*) AS status_change_count
FROM card_change_history
WHERE oldStatus IS NOT NULL
  AND oldStatus != newStatus
GROUP BY cardID
ORDER BY status_change_count DESC, card_id;

-- PART 2: Create a SQL query that indicates the number of status changes by card





