#Base Image to use
FROM python:3.9-buster

#Expose port 8080
EXPOSE 8080

#Copy Requirements.txt file into app directory
COPY src/requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

#Copy all files in current directory into app directory
COPY src/ /app


#Change Working Directory to app directory
WORKDIR /app/

ENTRYPOINT ["bash", "start.sh"]