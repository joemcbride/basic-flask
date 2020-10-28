FROM python:3.7-slim-buster

RUN pip install -U Flask

ENV FLASK_APP "main.py"

COPY ./src /

ENTRYPOINT ["python", "main.py"]