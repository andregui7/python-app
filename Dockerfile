FROM python:3.10-alpine
WORKDIR /src
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
COPY ./src /src
EXPOSE 5000
CMD ["python", "app.py"]