FROM ubuntu:14.04

MAINTAINER Miles Hutson

RUN apt-get update -y

RUN apt-get install -y  git\
                        python-dev\
                        python-setuptools

RUN easy_install pip

RUN git clone $GIT_PATH /opt/site

RUN cd /opt/site && git checkout dockerize && pip install -r requirements.txt

RUN mkdir /var/eb_log

ENV PROJECT_DIR /opt/site

RUN cd /opt/site && python profsUT/manage.py collectstatic --noinput\
                 && python profsUT/manage.py migrate --noinput\
                 && python profsUT/manage.py createsu

CMD gunicorn -c /opt/site/gunicorn_config.py profsUT.wsgi --access-logfile /var/eb_log/gunicorn_log

EXPOSE 8001