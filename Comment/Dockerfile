FROM debian:latest
RUN apt-get -y update &&\
apt-get -y install python3 python3-pip python3-cryptography
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["python3","main.py"]