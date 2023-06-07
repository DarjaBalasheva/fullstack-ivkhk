# Установка базового образа Python
FROM python:3.9

# Установка pipenv
RUN pip install pipenv

# Обновление пакетного менеджера и установка Git
RUN apt-get update && apt-get install -y git

# Установка зависимостей FastAPI
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода приложения
COPY . .

# Установка зависимостей с помощью pipenv
RUN pipenv install --system --deploy

# Запуск команды pip-sync
RUN pipenv shell

#Установка линтеров
RUN pre-commit install

# Запуск приложения FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
