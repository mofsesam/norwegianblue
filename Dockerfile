FROM python:3-alpine
RUN apk update
RUN pip install --upgrade pip

COPY ./service /service
RUN pip install -r /service/requirements.txt

EXPOSE 5000

CMD ["python3", "./service/DemoMicroservice.py"]