FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /fastAPI

COPY req.txt .

RUN apt update

RUN apt install -y uvicorn

RUN pip3 install --upgrade pip setuptools

RUN pip3 install --upgrade pip wheel

RUN pip3 install -r req.txt

COPY api_collections .

COPY app.py .

CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port 8000"]
