FROM python:3.6.2

LABEL maintainer="Zorex Salvo <zorexsalvo@gmail.com" \
      application="Blog API"

ENV PYTHONUNBUFFERED=1

RUN apt-get -y update

COPY requirements.txt /opt/
RUN pip install -r /opt/requirements.txt

COPY . /opt/
WORKDIR /opt/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
