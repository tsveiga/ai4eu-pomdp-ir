FROM ubuntu
MAINTAINER Tiago Veiga
ENV TZ=Europe/Oslo
ENV DEBIAN_FRONTEND noninteractive

COPY ./requirements.txt /requirements.txt
COPY src /pkg/src
COPY pomdp_ir_server.py java_factory.py model.proto /pkg/

RUN mkdir /pkg/models

RUN apt-get update && apt-get install -y \
    openjdk-8-jdk \
    python3-pip
RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

WORKDIR /pkg/src/java
RUN javac *java
RUN chmod +x compile_jar.sh
RUN ./compile_jar.sh

WORKDIR /pkg
RUN python3 -m grpc_tools.protoc --python_out=. --proto_path=. --grpc_python_out=. model.proto

ENTRYPOINT [ "python3","pomdp_ir_server.py" ]