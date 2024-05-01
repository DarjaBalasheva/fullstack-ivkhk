# Multimedia website of the thesis. Fullstack
<img src="https://github.com/DarjaBalasheva/fullstack-ivkhk/actions/workflows/my_workflow.yml/badge.svg">

This project was developed as part of an educational internship at IVKHK Kutsehariduskeskus. The project is a website for searching and viewing graduation projects of multimedia students. Additionally, a MySQL database was created to store data, along with a script for automatically recording project information into the database. The project was wrote in Python.

## Содержание
- [Description project](#description-project)
  - [Backend](#backend)
  - [Frontend](#frontend)
- [Requirements](#requirements)
- [Installing on mac os](#Installing-on-mac-os)
- [Setting](#setting)
- [Start](#start-project)
- [License](#license)

## Description project
### Backend
#### FastAPI:
This project is using the FastAPI framework. Jinja2Templates is utilizing for working with HTML pages and managing static files.
Routes is using the `@app.get` decorator, corresponding to different pages of the application. Request parameters: routes are utilizing query parameters such as `message` and `key`, which are passing into the handler functions. Default arguments are also using for query parameters if they are not explicitly specified.
Database interaction: Handler functions are interacting with the database by executing SQL queries to retrieve data. The asynchronous version of the `execute` function are using to execute queries. Additionally, `dictionary=True` is employed to retrieve results as dictionaries instead of tuples.
#### Docker:
Project is using Docker
#### Data Base:
Project is using DB MySQL
For connecting to DB importing mysql.connector.
Tables are creating for saving information. Primary and foreign keys are using in tables.
Unique values are creating to avoid dublicates.
#### phpMyAdmin:
phpMyAdmin installing with Docker for work in DB.
#### Pipfile:
Используется для управления зависимостями проекта.
#### Linters и pre-commit:
Linters black, autoflake, flake8 и pre-commit are using.
#### Swagger Configure:
Swagger are using to API documentation.
#### Virtual Environment
Virtual Environment are using to transfer secret data

## Frontend
Project is having simple UX/UI design, therefore it using CSS and HTML in Frontend with Jinja2Templates.
## Requirements
- Git
- Docker
- Docker-compose
- Python
- Pipenv

## Installing on mac os
- [Installing Python](https://www.python.org/downloads/macos/)
- [Installing Docker](https://www.docker.com/get-started/)
- Install Git with Homebrew.
  - Installing Homebrew
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
  - Installing GIT
    ```bash
    brew install git
    ```
- Cloning repository.
```bash
git clone git@github.com:DarjaBalasheva/fullstack-ivkhk.git
cd fullstack-ivkhk
```

- Installing pipenv
```bash
pip pipenv install
```
## Setting
### Setting env file
Create .env file in backend folder and set passwords:
```bash
# FastAPI
domen=your_domen

# MySQL
db_host=your_host
db_name=your_db_name
db_user_login=your_user_name
db_user_password=your_user_password

# phpMyAdmin
db_root_password=your_root_password
```
Change **your_domen**, **your_host**, **your_db_name**, **your_user_name**, **your_user_password**, **your_root_password** to your values.
### Настройка библиотек зависимостей
- Installing libraries from **Pipfile**. This command are creating virtualenv and are installing all libraries for project.
```bash
pipenv install
```
- Activate virtualenv pipenv
```bash
pipenv shell
```
### Setting linters and pre-commit
```bash
pre-commit install
```
## Start project
Run docker-compose:
```bash
docker-compose up -d
```
Run FastAPI
```bash
uvicorn main:app --reload
```

Project host: http://localhost:8000.

## License
This priject are using license MIT.
