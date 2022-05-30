FROM python:buster
WORKDIR /app
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . .
ENTRYPOINT ["python"]
CMD ["main.py"]