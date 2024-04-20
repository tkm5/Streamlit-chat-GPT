FROM python:3.12-slim

WORKDIR /app

COPY ./app /app
COPY ./requirements.txt /app

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "/app/main.py"]