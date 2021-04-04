release: flask db init
release: flask db migrate -m "Initial migration."
release: flask db upgrade
web: gunicorn event_scheduling_service:app

