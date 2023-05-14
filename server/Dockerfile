# FROM httpd:latest
# WORKDIR /app
# RUN apt-get update
# RUN apt-get install net-tools -y
# COPY . .
# # keep the container running
# ENTRYPOINT ["tail", "-f", "/dev/null"]

FROM ubuntu:latest
WORKDIR /app
RUN apt update
RUN apt install net-tools -y
RUN apt install iputils-ping -y
RUN apt install apache2 -y
RUN apt install apache2-utils -y
RUN apt clean
CMD ["apache2ctl", "-D", "FOREGROUND"]