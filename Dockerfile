FROM python:3.11-slim

COPY /app/app.py /app.py

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt

ENTRYPOINT [ "python", "/app.py" ]