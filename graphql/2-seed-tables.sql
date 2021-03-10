
DROP TYPE IF EXISTS process;
CREATE TYPE process AS ENUM ('ingestion', 'prediction');

--------------------------------------------------------------------------------
-- https://www.postgresqltutorial.com/postgresql-identity-column/
--------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS app.jobs (
    job_id SERIAL PRIMARY KEY NOT NULL,
    job_type PROCESS NOT NULL,
    job_started TIMESTAMP NOT NULL,
    job_ended TIMESTAMP NOT NULL,
    files TEXT[] NOT NULL,
    file_records INT[] NOT NULL
);
CREATE INDEX idx_jobs_1 ON app.jobs(job_id);

--------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS app.attributes (
    attribute_id SERIAL PRIMARY KEY NOT NULL,
    ingestion_id INT NOT NULL,
    entity_id TEXT NOT NULL,
    key TEXT NOT NULL,
    value JSON NOT NULL,
    FOREIGN KEY (ingestion_id) REFERENCES app.jobs(job_id)
);
CREATE INDEX idx_attributes_1 ON app.attributes(ingestion_id);
CREATE INDEX idx_attributes_2 ON app.attributes(entity_id);