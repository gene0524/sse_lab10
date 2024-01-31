FROM python:3.11

WORKDIR /python-flask

COPY /client_service /python-flask

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=/python-flask/api/app.py

CMD ["flask", "run", "--host=0.0.0.0"]