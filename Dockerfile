FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
  apache2 \
  python3-pip python3-dev \
  python3.7 \
  build-essential \
  python3.7 \
  wget

COPY server/index.html /var/www/html/index.html

RUN ln -s /etc/apache2/mods-available/cgi.load /etc/apache2/mods-enabled/

COPY . /usr/lib/cgi-bin
RUN chmod 755 /usr/lib/cgi-bin/server.py
RUN chmod 755 /usr/lib/cgi-bin/upload.py

WORKDIR /usr/lib/cgi-bin

# By default start up apache in the foreground, override with /bin/bash for iterative.
CMD ["/usr/sbin/apache2ctl", "-D",  "FOREGROUND"]