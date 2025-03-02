# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Upgrade pip and install the required packages
RUN pip install --upgrade pip && \
    pip install --no-cache-dir flask websockets

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable for Flask if needed
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["python", "app.py"]

# docker build -t websocket-checker .
# docker run -p 5000:5000 websocket-checker
