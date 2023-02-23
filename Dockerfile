# base image  
FROM python
# environment variable  
ENV DockerHOME=/home/app/webapp  

# making directory  
RUN mkdir -p $DockerHOME  

# current working directory  
WORKDIR $DockerHOME  
 
RUN pip install --upgrade pip  

# copy whole project to working directory. 
COPY . $DockerHOME  
# command to install all dependencies  
RUN pip install -r requirements.txt  
# port where the Django app runs  
EXPOSE 8000  
# start server  
CMD python manage.py runserver 