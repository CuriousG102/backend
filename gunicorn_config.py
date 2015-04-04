import multiprocessing

command = '/usr/local/bin/gunicorn'
pythonpath = 'opt/site/profsUT'
bind = '127.0.0.1:8001'
workers = multiprocessing.cpu_count()*2 + 1