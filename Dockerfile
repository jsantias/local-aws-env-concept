FROM python:3.9-buster

WORKDIR /app

COPY ./requirements.txt ./
COPY ./sender.py ./
COPY ./receiver.py ./
COPY ./upload.py ./
COPY ./filename_generator.py ./

RUN pip install -r ./requirements.txt

ENTRYPOINT [ "python" ]