FROM python:latest

# set the working directory in the container
#WORKDIR /code
Maintainer niteengadekar@gmail.com

# install dependencies
RUN python -m pip install --user boto3

# copy the content of the local src directory to the working directory
COPY attachment.py .
COPY index.html . 
# command to run on container start
CMD [ "python", "./attachment.py", "index.html" , "niteengadekar@gmail.com" ]
