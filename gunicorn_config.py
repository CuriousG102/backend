import multiprocessing

command = '/usr/local/bin/gunicorn'
pythonpath = '/opt/site/profsUT'
bind = '0.0.0.0:8001'
workers = multiprocessing.cpu_count()*2 + 1
worker_class = 'gevent'