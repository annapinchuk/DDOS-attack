FROM gcc:bullseye
WORKDIR /app
RUN apt-get update && apt-get install -y \
    iputils-ping \
    net-tools \
    && rm -rf /var/lib/apt/lists/*
COPY . .
WORKDIR /home/attacker_c
# RUN cd /home/attacker_c && gcc -o attacker attacker_c.c
CMD ["tail", "-f", "/dev/null"] # This is to keep the container running