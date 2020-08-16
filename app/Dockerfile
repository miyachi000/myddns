FROM python:3.6-buster as builder

WORKDIR /opt/app

COPY requirements.lock /opt/app
RUN pip3 install -r requirements.lock

RUN apt update \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY . /opt/app

EXPOSE 8082
CMD ["python3", "/opt/app/main.py"]
