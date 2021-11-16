FROM python:slim-buster
WORKDIR /app
COPY ["django_web_app/requirements.txt","./"]
EXPOSE 8000
RUN pip3 install -r requirements.txt