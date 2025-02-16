FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/
COPY ./requirements.txt ./
                                                   
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

CMD [ "python3", "consumer-service-1.py" ]