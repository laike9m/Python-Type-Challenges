FROM python:3.12-slim-bookworm

RUN pip install -U pip setuptools wheel
RUN pip install pdm
RUN apt-get update && apt-get install -y curl # for debug

WORKDIR /app

COPY . /app
RUN pdm install
EXPOSE 5000

CMD ["pdm", "startserver"]
