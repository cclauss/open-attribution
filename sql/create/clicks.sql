CREATE TABLE clicks
(
    id UUID DEFAULT generateUUIDv4(),
    event_time DateTime64(3, 'UTC'),
    store_id LowCardinality(String),
    network LowCardinality(String),
    campaign_name LowCardinality(String),
    campaign_id LowCardinality(String) DEFAULT '',
    ad_name LowCardinality(String) DEFAULT '',
    ad_id LowCardinality(String) DEFAULT '',
    ifa UUID,
    client_ip String DEFAULT '',
) ENGINE = MergeTree ORDER BY (store_id, network, event_time)

