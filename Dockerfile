#docker build --build-arg DockerHOME=/home/app/webapp --build-arg DockerPORT=8000 . -t dj_docker-v
#docker run -p 8000:8000 -v ~/.PYTHON/django_tests/dj_docker:/home/app/webapp dj_docker-v
# base image  
FROM python:3.10   
# declare the working directory.
# This will be the root directory of the Django app
# in the container 
ARG DockerHOME
# create work directory  
RUN mkdir -p $DockerHOME  
# 
COPY requirements.txt $DockerHOME
# set the provided directory as the location where 
# the application will reside within the container 
WORKDIR $DockerHOME  
# will no longer write .pyc files to disk  
ENV PYTHONDONTWRITEBYTECODE 1
# python output i.e. the stdout and stderr streams are sent straight
# to terminal (e.g. your container log) without being first buffered
# and that you can see the output of your app (e.g. django logs) in real time.
ENV PYTHONUNBUFFERED 1  
# install dependencies  
RUN pip install --upgrade pip  
# run this command to install all dependencies  
RUN pip install -r requirements.txt
# start server with 0.0.0.0:port
ARG DockerPORT
ENV PORT=$DockerPORT
CMD python3 manage.py runserver 0.0.0.0:$PORT