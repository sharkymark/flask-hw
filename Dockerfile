# Define the argument before its first use
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# get ps utility in the container
RUN apt-get update && apt-get install -y procps

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5001 available to the world outside this container
# Default 5000 conflicts with AirPlay on my mac
EXPOSE 5001

# Define environment variable
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001

# Run app.py when the container launches
CMD ["flask", "run"]

