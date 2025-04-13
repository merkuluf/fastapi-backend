.PHONY: lint
lint:
	poetry run ruff check
	poetry run mypy ./src ./bin ./bot

.PHONY: up_local
up_local:
	docker compose -f docker-compose.local.yaml up --build -d