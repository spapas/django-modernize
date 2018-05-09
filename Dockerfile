FROM python:3.6

WORKDIR /

copy requirements.txt requirements.txt

#RUN apt-get update && apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev python-dev

RUN pip install -r requirements.txt

EXPOSE 8000
#ENV DJANGO_SETTINGS_MODULE mailer_server.settings.docker

WORKDIR /code/

