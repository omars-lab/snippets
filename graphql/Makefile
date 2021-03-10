
start:
	# https://hub.docker.com/_/postgres
	docker run -d -p 5432:5432 \
		-e "POSTGRES_PASSWORD=password" \
		-e 'POSTGRES_USER=postgres' \
		-v $(PWD)/:/seed/ \
		postgres
	sleep 5

stop:
	# (docker ps -f ancestor=postgres -f status=running -q | xargs -n1 docker inspect ) | jq '.[0].NetworkSettings.Ports[("5432/tcp")][0].HostPort'
	docker ps -f ancestor=postgres -f status=running -q | xargs -n 1 docker stop

seed:
	docker exec -it $$(docker ps -f ancestor=postgres -f status=running -q | head -n 1) psql -U postgres -f /seed/1-seed-schemas.sql
	docker exec -it $$(docker ps -f ancestor=postgres -f status=running -q | head -n 1) psql -U postgres -f /seed/2-seed-tables.sql
	docker exec -it $$(docker ps -f ancestor=postgres -f status=running -q | head -n 1) psql -U postgres -f /seed/3-seed-users.sql
	docker exec -it $$(docker ps -f ancestor=postgres -f status=running -q | head -n 1) psql -U postgres -f /seed/4-seed-data.sql

query: 
	docker exec -it $$(docker ps -f ancestor=postgres -f status=running -q | head -n 1) psql -U postgres -f /seed/5-query-data.sql

restart: stop start seed query

exec: 
	docker exec -it $$(docker ps -f ancestor=postgres -f status=running -q | head -n 1) bash

run:
	cd app && uvicorn main:app --reload

# https://github.com/graphql/graphiql
