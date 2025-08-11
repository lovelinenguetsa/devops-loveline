# Dockerfile - Instructions to package our app into a container image

# Stage 1: Use a lightweight Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency list
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port 5000 so Kubernetes/Docker knows where to send traffic
EXPOSE 5000

# Command to run when container starts
CMD ["python", "app.py"]
