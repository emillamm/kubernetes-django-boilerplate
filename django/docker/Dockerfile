from ubuntu:14.04
MAINTAINER Emil Lamm Nielsen

RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update --fix-missing
RUN apt-get install -y build-essential git libpq-dev
RUN apt-get install -y python python-dev python-setuptools
RUN apt-get install -y python-pip python-virtualenv
RUN apt-get install -y nginx supervisor
RUN apt-get install -y binutils libpq-dev libproj-dev gdal-bin

RUN service supervisor stop
RUN pip install supervisor-stdout
RUN virtualenv /opt/venv
ADD requirements/common.txt /opt/venv/requirements/common.txt
ADD requirements/development.txt /opt/venv/requirements/development.txt
ADD requirements/production.txt /opt/venv/requirements/production.txt
RUN /opt/venv/bin/pip install -r /opt/venv/requirements/production.txt

EXPOSE 8000
EXPOSE 5672

ENV PYTHONPATH /opt/app:$PYTHONPATH
ENV DJANGO_SETTINGS_MODULE DJANGO_PROJECT_NAME.settings
ENV TOS_CURRENT_VERSION 1
ENV DEBUG false

ADD ./supervisord.conf /etc/supervisord.conf
ADD ./nginx.conf /etc/nginx/nginx.conf
RUN service nginx stop
ADD . /opt/app
RUN /opt/venv/bin/python /opt/app/manage.py collectstatic --noinput
COPY ./docker-entrypoint.sh /opt

ENTRYPOINT ["/opt/docker-entrypoint.sh"]