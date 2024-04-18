FROM python:3.10.12
WORKDIR /app
RUN apt-get update -y
RUN apt-get upgrade -y
COPY ./requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./itproger1 ./itproger1
CMD gunicorn -w 3 --chdir ./itproger1 itproger1.wsgi --bind 0.0.0.0:8000