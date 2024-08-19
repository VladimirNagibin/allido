python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input
cp -r /app/collected_static/. /static/static/

gunicorn allido_backend.wsgi:application --bind 0.0.0.0:8000
 