# Docker-команда FROM вказує базовий образ контейнера
# Наш базовий образ - це Linux з попередньо встановленим python-3.10
FROM python:3.10

# Встановимо змінну середовища
ENV APP_HOME /app

# Встановимо робочу директорію усередині контейнера
WORKDIR $APP_HOME/bot_assistant

# Скопіюємо інші файли до робочої директорії контейнера
COPY . .

# Встановимо залежності усередині контейнера
RUN pip install -r requirements.txt

# Позначимо порт де працює програма всередині контейнера
EXPOSE 5000

# Запустимо нашу програму всередині контейнера
ENTRYPOINT ["python", "main.py"]