FROM python:3.6

WORKDIR /app

ADD . /app

RUN pip3 install -r Requirements.txt

CMD ["gunicorn", "--bind", ":8000","wsgi:app"]
