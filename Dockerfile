FROM python:3.9-buster

WORKDIR /app

COPY ./requirements.txt ./
COPY ./upload.py ./
COPY ./filename_generator.py ./

RUN pip install -r ./requirements.txt

ENTRYPOINT [ "jurigged" ]