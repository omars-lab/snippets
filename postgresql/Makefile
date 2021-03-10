run:
	docker run -P -d -e POSTGRES_PASSWORD=password postgres

test-int-array:
	PGUSER='postgres' \
	PGPASSWORD='password' \
	PGHOST='localhost' \
	PGPORT='$(shell (docker ps -f ancestor=postgres -f status=running -q | xargs -n1 docker inspect ) | jq -r '.[0].NetworkSettings.Ports[("5432/tcp")][0].HostPort')' \
	PGDATABASE='postgres' \
	psql -f test-floats-schema.sql

