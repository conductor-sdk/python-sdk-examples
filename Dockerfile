FROM python:3.11-alpine as piton
RUN mkdir /package
COPY /requirements.txt /package/
COPY /examples /package/examples
WORKDIR /package
RUN python3 -m pip install -r requirements.txt

FROM piton as test
WORKDIR /package/examples
RUN python3 main.py
