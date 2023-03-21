FROM python:3.8-slim-buster

WORKDIR /python/app 

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . . 

CMD [ "python3", "-m" , "flask", "run", "--port=8080","--host=127.0.0.1"]