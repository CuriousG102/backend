FROM curiousg102/profsut_django

MAINTAINER Miles Hutson

EXPOSE 8001

CMD cd /opt/site && python profsUT/manage.py collectstatic --noinput\
                 && python profsUT/manage.py migrate --noinput\
                 && python profsUT/manage.py createsu\
                 && gunicorn -c /opt/site/gunicorn_config.py profsUT.wsgi --access-logfile /var/eb_log/gunicorn_log