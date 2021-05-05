# Makefile for the django project.

SHELL := /bin/bash

.PHONY: all help build test clean dev dbshell install docker-build heroku-build

help:
	@echo "$$(tput bold)Available subcommands:$$(tput sgr0)";echo;sed -ne"/^## /{h;s/.*//;:d" -e"H;n;s/^## //;td" -e"s/:.*//;G;s/\\n## /---/;s/\\n/ /g;p;}" ${MAKEFILE_LIST}|LC_ALL='C' sort -f|awk -F --- -v n=$$(tput cols) -v i=29 -v a="$$(tput setaf 6)" -v z="$$(tput sgr0)" '{printf"%s%*s%s ",a,-i,$$1,z;m=split($$2,w," ");l=n-i;for(j=1;j<=m;j++){l-=length(w[j])+1;if(l<= 0){l=n-i-length(w[j])-1;printf"\n%*s ",-i," ";}printf"%s ",w[j];}printf"\n";}'

## Building, testing, and deploy to development server
all: test dev

## Build the project  
build:
	python manage.py makemigrations
	python manage.py migrate
# python manage.py collectstatic

## Run all unit tests
test: build
	python manage.py test

clean:
	rm db.sqlite3

## Build and run the project on development server
dev: build 
	python manage.py runserver

## Update database and spawn a dbshell 
dbshell: build
	python manage.py dbshell

## Install the project dependencies and create virtual environment
install:
	@pipenv install -r requirements.txt

## Build a docker image [Docker]	
docker-build: 
	sudo docker build -t app .

## Run the docker image [Docker]
docker-run: 
	sudo docker run --name app -p 8000:8000 -d app

## Build and deploy to production server [Heroku]
heroku-build: test 
	@echo "$$(tput bold)$$(tput setaf 1)Not implemented $$(tput sgr 0)"	