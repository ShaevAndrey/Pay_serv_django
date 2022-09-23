FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /test_task
COPY . /test_task/
RUN pip install -r requirements.txt
CMD gunicorn test_task.wsgi:application --bind 0.0.0.0:$PORT