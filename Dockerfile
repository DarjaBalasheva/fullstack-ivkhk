# Установка базового образа Python
FROM python:3.11

# Установка pipenv
RUN pip install pipenv

# Установка зависимостей FastAPI
WORKDIR /app

# Копирование Pipfile и Pipfile.lock
COPY Pipfile Pipfile.lock ./

# Установка зависимостей с помощью pipenv
RUN pipenv install --system --deploy

# Копирование остального кода приложения
COPY . .

WORKDIR backend

# Запуск приложения FastAPI
CMD uvicorn main:app --host 0.0.0.0 --port 8000
