# Use a Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app
# Install system deps
RUN apt-get update && apt-get install -y build-essential
# Copy requirements
COPY requirements.txt .
# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt
# Copy the whole backend code
COPY . .
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Expose Django port
EXPOSE 8000
# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
