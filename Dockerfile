FROM python:3.10
LABEL author="Peter Götz (peter.goetz@pgoetz.de)"

WORKDIR /torpydo

COPY requirements.txt /torpydo

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
