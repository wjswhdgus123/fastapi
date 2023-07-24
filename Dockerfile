# Base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the FastAPI app file to the container's working directory
COPY main.py .

# Install required dependencies
RUN pip install fastapi uvicorn

# Expose the port that FastAPI will be running on
EXPOSE 80

# Command to start the FastAPI server using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]