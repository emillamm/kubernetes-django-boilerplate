#!/bin/bash
if [ "$IS_WORKER" == "true" ]; then
	echo 'starting celery worker';
	export C_FORCE_ROOT=1
	/opt/venv/bin/celery -A DJANGO_PROJECT_NAME worker -l info -B -s /opt/celerybeat-schedule
else
	echo 'starting gunicorn web server';
	supervisord -c /etc/supervisord.conf -n
fi