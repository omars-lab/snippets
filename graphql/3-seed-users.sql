 -- DEFINE USER
DROP USER IF EXISTS rw_user ;
CREATE USER rw_user PASSWORD 'password';

-- R Table Permissions
GRANT CONNECT ON DATABASE postgres TO rw_user;
GRANT USAGE ON SCHEMA app TO rw_user;
GRANT SELECT ON ALL TABLES IN SCHEMA app TO rw_user;
-- W Table Permissions
GRANT INSERT ON ALL TABLES IN SCHEMA app TO rw_user;
GRANT UPDATE ON ALL TABLES IN SCHEMA app TO rw_user;
GRANT DELETE ON ALL TABLES IN SCHEMA app TO rw_user;
-- GRANT DELETE ON app.specific_table TO rw_user;
-- Sequence Permissions
GRANT USAGE ON ALL SEQUENCES IN SCHEMA app TO rw_user;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA app TO rw_user;

--------------------------------------------------------------------------------

DROP USER IF EXISTS read_only_user ;
CREATE USER read_only_user PASSWORD 'password' ;
-- R Table Permissions
GRANT CONNECT ON DATABASE postgres TO read_only_user;
GRANT USAGE ON SCHEMA app TO read_only_user;
GRANT SELECT ON ALL TABLES IN SCHEMA app TO read_only_user;