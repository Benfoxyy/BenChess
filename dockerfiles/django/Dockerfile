FROM python:3.11-bullseye

LABEL maintainer="benxfoxy@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

COPY ./core /app

COPY ./stockfish /app/stockfish

RUN chmod +x /app/stockfish/stockfish-ubuntu-x86-64-modern