# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Expose the port the app runs on
EXPOSE 5000

# Copy application code
COPY app.py .

# Run the app
CMD ["python", "app.py"]
