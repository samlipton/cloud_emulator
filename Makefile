.PHONY: up down reset logs ps test

up:
	docker compose up -d --build

down:
	docker compose down

reset:
	docker compose down -v
	docker compose up -d --build

logs:
	docker compose logs -f

ps:
	docker compose ps

test: up
	pip install -q -r tests/integration/requirements.txt
	pytest tests/integration
