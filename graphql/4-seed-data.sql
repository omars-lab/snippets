-- Samples:
--      Timestamp: '2018-12-31T06:00:00'
--      INT[]:  ARRAY [0, 0, 5, 3, 6, 2, 1, 0, 0, 0, 0, 5]

--------------------------------------------------------------------------------

INSERT INTO app.jobs (
    job_id, job_type, job_started, job_ended, files, file_records
)
VALUES (
    1, 
    'ingestion', 
    NOW() - '1 minute'::interval, 
    NOW(), 
    '{"file-a.csv", "file-b.csv"}', 
    ARRAY [100, 200]
);

--------------------------------------------------------------------------------

INSERT INTO app.attributes (
    ingestion_id, entity_id, key, value
)
VALUES 
    ( 1, 'e1', 'knows', '{"entity": "e2"}'::json ),
    ( 1, 'e2', 'knows', '{"entity": "e1"}'::json )
    ;