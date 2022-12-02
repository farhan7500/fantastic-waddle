from ubuntu:latest
RUN apt update
RUN apt install -y git
RUN apt install -y python3
RUN git clone https://github.com/farhan7500/fantastic-waddle

WORKDIR fantastic-waddle

CMD  python3 intro.py

