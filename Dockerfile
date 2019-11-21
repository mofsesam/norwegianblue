FROM python:3-alpine
RUN apk update
RUN pip install --upgrade pip

COPY ./service/requirements.txt /service/requirements.txt
RUN pip install -r /service/requirements.txt

COPY ./service /service
WORKDIR /service/

EXPOSE 5000

CMD ["python3", "norwegianblue.py"]