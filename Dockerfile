FROM python:2.7-alpine
# add the build dependencies

RUN apk update && pip install kazoo

# copy current source code into the container
ADD . /home/barrier
WORKDIR /home/barrier

CMD /bin/sh 