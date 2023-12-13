# Use an official Python runtime as a parent image
FROM python:3.8

# Install Poppler and Tesseract
RUN apt-get update && \
    apt-get install -y \
        poppler-utils \
        tesseract-ocr \
        libtesseract-dev \
        ffmpeg \
        libsm6 \
        libxext6 \
        libgl1-mesa-glx  # Add this line to install libGL.so.1 dependency

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create and activate a virtual environment
RUN python -m venv venv && \
    . venv/bin/activate

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python", "main.py"]
