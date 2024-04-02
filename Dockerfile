FROM python:3

WORKDIR /drf_project

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .



