uwsgi \
--socket /var/run/uwsgi.sock \
--chmod-socket=666 \
--wsgi-file /usr/local/www/nginx/pyapp/wsgi.py \
--chdir /usr/local/www/nginx/pyapp/
