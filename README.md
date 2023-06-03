# Multimedia lõputöö site. Fullstack
<img src="https://github.com/DarjaBalasheva/fullstack-ivkhk/actions/workflows/my_workflow.yml/badge.svg">

Этот проект был разработан в ракмках учебной практики в IVKHK Kutsehariduskeskus.
Проект представляет собой сайт для поиска и просмотра выпускных работ студентов направления мультимедиа.
Также была создана БД mysql для хранения данных и скрипт для автоматической записи инормации о проектах в БД.
Проект написан на Python.

## Содержание
- [Описание проекта](#описание-проекта)
  - [Backend](#backend)
  - [Frontend](#frontend)
- [Требования](#требования)
- [Установка на mac os](#установка-на-mac-os)
- [Настройка](#настройка)
- [Запуск](#запуск-проекта)
- [Лицензия](#лицензия)

## Описание проекта
### Backend
#### FastAPI: 
В данном проекте была реализована работа с фреймвороком FastAPI для создания веб-страниц.
Есть основной экземпляр FastAPI приложения app, который подключается к базе данных и монтирует статические файлы и медиафайлы.
Подключен Jinja2Templates для работы с HTML-шаблонами и монтажа статических файлов.
Определены маршруты с использованием декораторов @app.get, которые соответствуют различным страницам приложения.
Определены параметры запроса: маршруты используют параметры запроса, такие как message и key, которые передаются в функции обработчика. Также используются параметры запроса с аргументами по умолчанию, если они не указаны явно.
Работа базой данных: функции обработчика взаимодействуют с базой данных, выполняя SQL-запросы для извлечения данных. Используется асинхронная версия функции execute для выполнения запросов. Также используется словарь dictionary=True, чтобы получить результаты в виде словарей вместо кортежей.
#### Docker: 
Проект использует Docker для контейниризации и развертывания установки mysql и phpmyadmin.
#### База данных: 
Проект использует базу данных MySQL для хранения и управления данными.
Был импортирован модуль mysql.connector для работы с базой данных MySQL.
Создано несколько таблиц для хранения информации и настроены внешние ключи для связи таблиц.
Созданы уникальные значения для некоторых параметров с целью избежания повторов и должной работы скрипта по атовмматической записи информации в БД.
#### phpMyAdmin:
Установлен phpMyAdmin в докер-контейнере для работы с БД.
#### Pipfile: 
Используется для управления зависимостями проекта.
#### Linters и pre-commit: 
Настроены линтеры black, autoflake, flake8 и pre-commit для анализа и форматирования кода.
#### Swagger Configure: 
В проекте настроена документация API с помощью Swagger.
Хотя фреймфорк FAstAPI автоматически создает документацию проекта, я решила создать свой swagger.yml для изучения принципа работы с ним.
#### Virtual Environment
Используются переменные окружения для передачи данных при создании БД и подключении к ней.

## Frontend
Во фронте были реализованы CSS и HTML с ипользованием шаблонизатора Jinja2Templates для header.
В данномпроектея хотела глубже ознакомится с возможностями CSS и HTML, поэтому не использовала Java
## Требования
- Git
- Docker
- Docker-compose
- Python
- Pipenv

## Установка на mac os
- [Установка Python](https://www.python.org/downloads/macos/)
- [Установка Docker](https://www.docker.com/get-started/)
- Установите Git, если он ещё не установлен с помощью Homebrew.
  - Установка Homebrew
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
  - Установка GIT
    ```bash
    brew install git
    ```
- Клонирование репозитория.
```bash
git clone git@github.com:DarjaBalasheva/fullstack-ivkhk.git
cd fullstack-ivkhk
```

- Установка библиотеки зависимостей
```bash
pip pipenv install
```
## Настройка
### Настройка env файла
Перед запуском проекта необходимо настроить переменные окружения.
Потребуется создать файл .env в каталоге backend проекта и указать следующие переменные:
```bash
# Настройки FastAPI
domen=your_domen

# Настройки базы данных MySQL
db_host=your_host
db_name=your_db_name
db_user_login=your_user_name
db_user_password=your_user_password

# Настройки phpMyAdmin
db_root_password=your_root_password
```
Необходимо заменить **your_domen**, **your_host**, **your_db_name**, **your_user_name**, **your_user_password**, **your_root_password** на соответсвующие значения.
### Настройка библиотек зависимостей
- Установка зависимостей, указанных в **Pipfile**. Эта команда создаст виртуальное окружение и установит все зависимости, указанные в Pipfile, в это окружение.
```bash
pipenv install
```
- Активация виртуального окружение pipenv
```bash
pipenv shell
```
Виртуальное окружение настроено. С помощью pipenv и установлены все зависимости, указанные в Pipfile.
Вы можете выполнять команды и запускать приложение внутри виртуального окружения.
После клонирования репозитория и установки зависимостей с помощью **pipenv**, не нужно использовать **pip** для установки или управления зависимостями.
Вместо этого используйте команды **pipenv install** и **pipenv uninstall** для добавления или удаления зависимостей.
### Настройка линтеров и pre-commit
```bash
pre-commit install
```
## Запуск проекта
Запустите Docker-контейнеры с помощью docker-compose:
```bash
docker-compose up -d
```
Запустите FastAPI
```bash
uvicorn main:app --reload
```
После успешного запуска контейнеров вы сможете получить доступ к веб-приложению FastAPI по адресу http://localhost:8000.

Узнать, можно ли в контейнерах запустить композе, установку дб и запуск FastAPI

## Лицензия
Этот проект лицензирован по лицензии MIT.
 
