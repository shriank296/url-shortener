source $(poetry env info --path)/bin/activate
docker-compose build
docker-compose up -d
alembic revision --autogenerate -m "create url_mapper table"
alembic upgrade head