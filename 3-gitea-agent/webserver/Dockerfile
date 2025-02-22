# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Install watchdog to use watchmedo
#RUN --mount=type=cache,target=/root/.cache/pip pip install watchdog==6.0.0

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

# Run the application with watchmedo for automatic reloading on changes
#ENTRYPOINT ["watchmedo", "auto-restart", "--directory=.", "--pattern=*.py", "--recursive", "--"]
CMD ["python", "main.py"]
