FROM ubuntu:18.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

COPY /ddc/. /SASDdc

RUN apt-get update -y  && \
    apt-get install -y python3 python3-flask python3-pip


RUN python3 -m pip install -r /SASDdc/requirements.txt



EXPOSE 8080
WORKDIR /SASDdc
CMD python3 app.py 
