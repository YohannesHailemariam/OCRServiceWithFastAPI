# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install Tesseract OCR
RUN apt-get update && apt-get install -y tesseract-ocr libtesseract-dev

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Run FastAPI server with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
