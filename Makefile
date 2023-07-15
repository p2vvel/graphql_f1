build_db_container:
	docker build -t f1db ./db --no-cache

run_db_dev:
	docker run -d -p3306:3306 --restart=unless-stopped -e MYSQL_DATABASE=f1 -e MYSQL_ROOT_PASSWORD=1234 --name f1db f1db

run_server:
	uvicorn api.app:app --reload