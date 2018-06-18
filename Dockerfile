FROM python:latest

COPY config/python/requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY src /srv

WORKDIR /srv

RUN chmod +x start.sh

ENTRYPOINT [ "./start.sh" ]