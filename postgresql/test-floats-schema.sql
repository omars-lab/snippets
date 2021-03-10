CREATE SCHEMA IF NOT EXISTS personal;
DROP TABLE IF EXISTS personal.int_array_test;
CREATE TABLE IF NOT EXISTS personal.int_array_test (
    int_array INT[] NOT NULL
);
INSERT INTO personal.int_array_test
    (int_array)
VALUES
    ('{1,2,3}');
    -- ('{1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9}');
SELECT * FROM personal.int_array_test;
