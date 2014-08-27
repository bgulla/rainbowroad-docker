FROM ubuntu:14.04
MAINTAINER Brandon Gulla <brandon@brandongulla.com>
RUN apt-get -y update && apt-get -y install python

#ADD colors.txt /colors.txt
ADD bin /bin
ADD lib /lib
ADD startWebServer.sh /startWebServer.sh
EXPOSE 8001

#CMD echo "Yo Dawg. Here I am, rock you like a hurricane."
CMD /startWebServer.sh
