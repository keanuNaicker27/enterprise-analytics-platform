-- Final aggregation in Azure for Power BI reporting
CREATE OR ALTER VIEW gold_layer.user_activity_summary AS
SELECT 
    user_id,
    COUNT(event_id) AS total_events,
    MAX(event_time) AS last_active,
    source_system
FROM dbo.processed_events
GROUP BY user_id, source_system;
