# Define the argument before its first use
FROM python:3.13-slim

# get ps utility in the container
RUN apt-get update && apt-get install -y procps curl net-tools htop ssh git bzip2

COPY requirements.txt .
 
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


