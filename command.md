source $(poetry env info --path)/bin/activate
docker-compose build
docker-compose up -d