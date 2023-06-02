FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY .env /app/.env
# COPY __init__.py /app/__init__.py
COPY gpt_interact.py /app/gpt_interact.py
COPY /model/. /app/model/
COPY main.py /app/main.py

CMD ["python", "main.py"]
