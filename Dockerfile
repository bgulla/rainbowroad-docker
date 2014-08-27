FROM ubuntu
MAINTAINER Brandon Gulla <brandon@brandongulla.com>
RUN apt-get -y update && apt-get -y install python

ADD colors.txt /colors.txt
ADD webserver.py /webserver.py
ADD pickacolor.py /pickacolor.py


CMD echo "Yo Dawg. Here I am, rock you like a hurricane."
