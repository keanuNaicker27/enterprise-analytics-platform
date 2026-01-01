
SELECT 
    event_name,
    COUNT(DISTINCT user_id) as unique_users,
    TIMESTAMP_TRUNC(event_time, HOUR) as event_hour
FROM `external_aws_connection.processed_data_table`
GROUP BY 1, 3
ORDER BY event_hour DESC;
