# 2900G6

## Introduction
Fridge Friend is a Django web application that makes it easy for an user to create, mantain and view their stored ingredients. With Fridge Friend, the user will be given recipe suggestions based on their stored ingredients. In addition, Fridge Friend offers the feature for the user to create and matain their own shopping list. Recipes ingredients can be added automatically with a simple button push into the users shopping list, meaning the missing ingredients that the users doesn't have yet! 

## Requirements
### Runtime
- python = 3.8
- asgiref = 3.3.1
- crispy-bootstrap5 = 0.3.1
- dj-database-url = 0.5.0
- django-crispy-forms = 1.11.2
- django-extensions = 3.1.3
- django = 3.1.5
- fontawesome-free = 5.15.3
- gunicorn = 20.1.0
- iniconfig = 1.1.1
- pillow = 8.2.0
- psycopg2-binary = 2.8.6
- python-dateutil = 2.8.1
- pytz = 2020.5
- six = 1.16.0
- sqlparse = 0.4.1
- whitenoise = 5.2.0

### Development
- pytest = 6.2.4
- coverage = 5.5
- pytest-cov = 2.12.0
- pytest-django = 4.3.0
- django-coverage-plugin = 1.8.0

## Getting Started
This is an example of how you may give instructions on setting up your project locally. To get a local copy up and running follow these simple example steps.

### Prerequisites
Download and install the latest pip and pipenv versions in order to build the project locally on the computer.
* pip3
  ```bash
  sudo apt-get install python3-pip
  ```
* pipenv
  ```bash
  pip3 install pipenv
  ```

### Installation 

1. Clone the repository and check out the master branch:
  ```bash
  git clone https://github.com/HakonVA/2900G6.git
  ```
2. Enter the repository: 
  ```bash
  cd 2900G6/
  ```
3. Built project using pipenv:
  ```bash
  make install
  ```  
  ```bash
  make dev-install
  ```  
4. To activate this project's virtualenv, run pipenv shell:
  ```bash
  pipenv shell
  ```
5. For information about subcommands:   
  ```bash
  make help
  python manage.py
  ```

## License

Distributed under the MIT License. See `LICENSE` for more information.
