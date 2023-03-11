FROM python:3.11-slim

COPY /app/app.py /app.py

COPY requirements.txt /requirements.txt

RUN apt update && apt install -y libwebp-dev && rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r /requirements.txt

ENTRYPOINT [ "python", "/app.py" ]