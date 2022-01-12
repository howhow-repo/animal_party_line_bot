FROM python:3.8

# project src
WORKDIR /code
COPY requirements.txt /code/
RUN python -m pip install --upgrade pip
RUN apt-get update -y
RUN apt-get install gdal-bin -y
RUN pip install -r requirements.txt
COPY . /code/


# setup djngo
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
