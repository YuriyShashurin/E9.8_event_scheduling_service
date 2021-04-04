release: set FLASK_APP=manage.py
release: alembic revision --autogenerate -m "initial migration"
release: alembic upgrade head
web: python manage.py 0.0.0.0:$PORT
