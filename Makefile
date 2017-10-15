.PHONY: docker_prepare _docker_prepare

docker_prepare:
	docker exec -it $(shell docker ps -q -f name=web_1) /bin/bash -c "python manage.py keygen"
	docker exec -it $(shell docker ps -q -f name=web_1) /bin/bash -c "python manage.py migrate"
	docker exec -it $(shell docker ps -q -f name=web_1) /bin/bash -c "python manage.py createsuperuserauto"
