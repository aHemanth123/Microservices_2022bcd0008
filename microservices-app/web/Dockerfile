# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy application files
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expose the port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
