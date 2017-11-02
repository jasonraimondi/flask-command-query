default: build

npm-install:
	docker-compose run --rm javascript npm install

npm-install:
	docker-compose run --rm javascript npm install

build:
	docker-compose build

clean: stop
	docker-compose rm

down:
	docker-compose down

pull:
	docker-compose pull

push:
	docker-compose push

rebuild: down pull build npm-install start-force-recreate

restart: stop start

start:
	docker-compose up -d
	docker-compose ps

start-force-recreate:
	docker-compose up -d --force-recreate
	docker-compose ps

stats:
	docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.MemPerc}}\t{{.NetIO}}\t{{.BlockIO}}" --no-stream

stats-stream:
	docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.MemPerc}}\t{{.NetIO}}\t{{.BlockIO}}"

status:
	docker-compose ps

stop:
	docker-compose stop

tail:
	docker-compose logs -f

top:
	docker-compose top


.PHONY: build clean down pull push rebuild restart start stats stats-stream stop tail top
