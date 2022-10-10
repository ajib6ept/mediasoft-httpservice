install:
	poetry install

lint:
	poetry run flake8 mediasoft --exclude=migrations,mediasoft/settings.py

test:
	poetry run python manage.py test

test_coverage:
	poetry run coverage run --source='mediasoft' manage.py test
	poetry run coverage xml
	poetry run coverage report

start_server:
	poetry run python manage.py runserver
