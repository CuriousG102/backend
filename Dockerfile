FROM ubuntu:14.04

MAINTAINER Miles Hutson

RUN apt-get update -y

RUN apt-get install -y  git\
                        python-dev
                        python-setuptools

RUN easy_install pip

RUN git clone $GIT_PATH /opt/site

RUN cd /opt/site

RUN git checkout dockerize

RUN pip install -r requirements.txt

RUN mkdir /var/eb_log

RUN python profsUT/manage.py collectstatic

RUN python profsUT/manage.py migrate

CMD ["gunicorn", "-c gunicorn_config.py", "profsUT.wsgi", "--access-logfile /var/eb_log/gunicorn_log"]

EXPOSE 8001