FROM python:3.9-slim
WORKDIR /app

RUN apt-get update && apt-get upgrade -y 

COPY requirements.txt .

RUN pip3 install -r requirements.txt

# Set umask
RUN echo "umask 002" >> /etc/profile

# Changing permissions of existing files
RUN chmod -R 777 /app

EXPOSE 8501
