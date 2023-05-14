FROM python:3.10-bullseye
WORKDIR /app
RUN apt-get update
RUN apt-get install iputils-ping -y
RUN pip install scapy
COPY . .
WORKDIR /home/monitor
ENTRYPOINT ["tail", "-f", "/dev/null"]