#Base Image to use
FROM python:3.9-buster

RUN apt-get update
RUN apt-get install ffmpeg -y

#Expose port 8080
EXPOSE 8080

#Copy Requirements.txt file into app directory
COPY src/requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

#Copy all files in current directory into app directory
COPY src/ /app

#Change Working Directory to app directory
WORKDIR /app/

RUN bash get_contrib.sh

ENTRYPOINT ["bash", "start.sh"]