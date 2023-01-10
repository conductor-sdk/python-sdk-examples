FROM python:3.11-alpine as piton
RUN mkdir /package
COPY /requirements.txt /package/
COPY /examples /package/examples
WORKDIR /package
RUN python3 -m venv examples
RUN source examples
RUN python3 -m pip install -r requirements.txt

FROM piton as test
ARG KEY
ARG SECRET
ARG CONDUCTOR_SERVER_URL
ENV KEY=${KEY}
ENV SECRET=${SECRET}
ENV CONDUCTOR_SERVER_URL=${CONDUCTOR_SERVER_URL}
WORKDIR /package/examples
RUN python3 main.py
