# Makefile

.PHONY: run migrate migrations superuser install

# Start the development server
run:
	uv run python manage.py runserver

# Apply database migrations
migrate:
	uv run python manage.py migrate

# Create new migrations based on model changes
migrations:
	uv run python manage.py makemigrations

# Create a superuser for the admin panel
superuser:
	uv run python manage.py createsuperuser

# Install dependencies (useful if you clone the repo later)
install:
	uv sync

# Run tests (if you add them later)
test:
	uv run python manage.py test