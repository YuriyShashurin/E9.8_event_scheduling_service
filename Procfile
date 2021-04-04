release: flask db init
release: flask db migrate -m "Initial migration."
release: flask db upgrade
web: python app.py 0.0.0.0:$PORT
web: gunicorn app:app

