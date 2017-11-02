default: build

npm-install:
	cd docker; docker-compose run --rm javascript npm install

npm-install:
	cd docker; docker-compose run --rm javascript npm install

build:
	cd docker; docker-compose build

clean: stop
	cd docker; docker-compose rm

down:
	cd docker; docker-compose down

pull:
	cd docker; docker-compose pull

push:
	cd docker; docker-compose push

rebuild: down pull build npm-install start-force-recreate

restart: stop start

start:
	cd docker; docker-compose up -d
	cd docker; docker-compose ps

start-force-recreate:
	cd docker; docker-compose up -d --force-recreate
	cd docker; docker-compose ps

stats:
	cd docker; docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.MemPerc}}\t{{.NetIO}}\t{{.BlockIO}}" --no-stream

stats-stream:
	cd docker; docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.MemPerc}}\t{{.NetIO}}\t{{.BlockIO}}"

status:
	cd docker; docker-compose ps

stop:
	cd docker; docker-compose stop

tail:
	cd docker; docker-compose logs -f

top:
	cd docker; docker-compose top


.PHONY: build clean down pull push rebuild restart start stats stats-stream stop tail top
