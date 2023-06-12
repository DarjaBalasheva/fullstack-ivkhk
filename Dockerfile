# Установка базового образа Python
FROM python:3.11

# Установка pipenv
RUN pip install pipenv

# Установка зависимостей FastAPI
WORKDIR /app

# Копирование кода приложения
COPY . .

RUN pipenv lock

# Установка зависимостей с помощью pipenv
RUN pipenv install --system --deploy

# Запуск команды pip-sync
RUN pipenv sync --system