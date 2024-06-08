# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# run this before copying requirements for cache efficiency
RUN pip install --upgrade pip

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install  --verbose -r requirements.txt

# Copy project files to the working directory
COPY . /app/

# Copy the .env file
COPY .env /app/.env

# Copy the project code into the container
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Start the application
CMD ["gunicorn", "--timeout", "120", "django_blog.wsgi:application", "--bind", "0.0.0.0:8000"]
