ps:
	docker compose ps
up:
	docker compose up -d
shell:
	docker compose exec app bash
build:
	docker compose build --no-cache
down:
	docker compose down