network:
	docker network create conn || true

up:
	docker compose up --build -d

down: 
	docker compose down

run: network up