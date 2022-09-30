lint:
	@poetry run flake8 mediasoft --exclude=mediasoft/settings.py

test:
	poetry run python manage.py test
