# Pay_serv_django
Pay_serv_django


Запуск без Docker`a:

1. Установка зависимостей:  
pip install requirements.txt


2. Запуск сервера:
gunicorn test_task.wsgi:application --bind 0.0.0.0:8000


Запуск с Docker:

1. Создаём контейнер:
docker build -t web .

2. Запускаем контейнер:
docker run -d -e "PORT=8000" -p 8000:8000 web

Адрес веб-сервера:

https://shrouded-wave-99510.herokuapp.com/

маршруты:

/item/<int:id> Получить товар по id

/get_all_items/ Получить данные всех товаров

/bay/<int:id>/ Купить один товар по id

/bay_items/ Купить несколько товаров. Принимает массив товаров.
