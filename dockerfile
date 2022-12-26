FROM python:3.9.7-alpine
WORKDIR /weather-app-flask
ADD . /weather-app-flask
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "./app.py"]
