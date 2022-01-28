FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN apt-get update && apt-get install -y \
   python3-dev \
   default-libmysqlclient-dev \
   build-essential

COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
