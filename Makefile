build:
	docker-compose build
	docker ps -a

start:
	docker-compose up -d --build
	docker-compose restart backend
	docker ps -a

start-a:
	docker-compose up

stop:
	docker-compose down
	docker ps -a

restart: stop start

restart-a: stop build start-a

status:
	docker ps -a

clean: stop
	docker volume rm shortener_dev_volume
	docker volume ls

exec-backend:
	docker exec -it shortener_backend /bin/bash 

logs:
	docker logs shortener_backend
