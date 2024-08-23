FROM python:3.11

RUN pip install --upgrade pip

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn", "main:app"]