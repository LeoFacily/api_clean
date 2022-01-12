FROM python:3.9

WORKDIR /app

COPY . /app
ENV APP_NAME=docker_fast_api
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]