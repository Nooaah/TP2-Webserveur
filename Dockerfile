FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
EXPOSE 80
CMD ["python3", "-V"]
CMD ["python3", "app.py"]
