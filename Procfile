release: set FLASK_APP=manage.py
release: flask db migrate -m "Initial migration."
release: flask db upgrade
web: gunicorn app:app

