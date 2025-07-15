# Use official Python image
FROM python:3.12-slim

# Set working dir inside container
WORKDIR /app

# Copy everything
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 for Cloud Run
EXPOSE 8080

# Run your Flask app
CMD ["python", "app.py"]
