FROM python:3.10-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
        build-essential \
        default-libmysqlclient-dev \
        pkg-config \
        libmariadb-dev-compat \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["python3", "server.py"]
