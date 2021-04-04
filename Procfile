release: set FLASK_APP=manage.py
release: flask db migrate -m "Initial migration."
release: flask db upgrade
web: flask run 0.0.0.0:$PORT
