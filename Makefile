# Makefile for the django project.

SHELL := /bin/bash

.PHONY: help all migrate test run coverage clean clean-pyc clean-test clean-db install dev-install docker-build docker-run

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

all: migrate test run ## Make, migrate, test, and deploy to dev server

migrate: ## Make and run migrations 
	python manage.py makemigrations
	python manage.py migrate

test: ## Run unit tests
	python manage.py test

run: migrate ## Build and deploy to dev server
	python manage.py runserver

coverage: ## Make a coverage report html
	pytest --cov=project --cov-report=html

clean: clean-pyc clean-test clean-db ## Remove test, coverage, db, and Python artifacts

clean-pyc: 
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov

clean-db:
	rm db.sqlite3

install: ## Install dependencies into a virtual environment
	pipenv install -r requirements.txt

dev-install: ## Install dev dependencies into a virtual environment
	pipenv install -r dev-requirements.txt

docker-build: ## Build source to a docker image [Docker]	
	docker build -t app .

docker-run: ## Run the docker image [Docker]
	docker run --rm --name app -p 8000:8000 app