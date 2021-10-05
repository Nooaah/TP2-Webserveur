FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
RUN apt-get update
RUN apt-get install -y
RUN apt-get install p7zip -y
RUN apt-get install curl -y
EXPOSE 5000
