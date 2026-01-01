-- Create Schema for logical separation
CREATE SCHEMA IF NOT EXISTS gold_layer;

-- 1. Create the Main Fact Table
CREATE TABLE IF NOT EXISTS gold_layer.fact_user_events (
    event_id        VARCHAR(50)   NOT NULL,
    event_time      TIMESTAMP     NOT NULL,
    user_id         VARCHAR(20)   NOT NULL,
    event_type      VARCHAR(50),
    source_system   VARCHAR(50),
    ip_address      VARCHAR(45),
    processed_at    TIMESTAMP     DEFAULT SYSDATE
)
DISTSTYLE KEY
DISTKEY (user_id)  -- Optimizes joins with User Dim tables
SORTKEY (event_time); -- Optimizes time-series filtering

-- 2. Staging Table for Ingestion
CREATE TEMP TABLE stage_user_events (LIKE gold_layer.fact_user_events);

-- 3. Copy Command (Template for your Documentation)t
/*
COPY stage_user_events
FROM 's3://enterprise-data-lake-raw/processed_data/'
IAM_ROLE 'arn:aws:iam::123456789012:role/RedshiftS3Role'
FORMAT AS PARQUET;
*/

-- 4. Final Aggregation View for Business Intelligence
CREATE OR REPLACE VIEW gold_layer.v_daily_event_summary AS
SELECT 
    TRUNC(event_time) as event_date,
    event_type,
    COUNT(DISTINCT user_id) as unique_active_users,
    COUNT(event_id) as total_event_volume
FROM gold_layer.fact_user_events
GROUP BY 1, 2;
