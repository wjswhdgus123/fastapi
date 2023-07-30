# Base image
FROM python:3.9
# Set the working directory inside the container
WORKDIR /code

# Copy the FastAPI app file to the container's working directory

COPY ./requirements.txt /code/requirements.txt
# Install required dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
# Expose the port that FastAPI will be running on
EXPOSE 80

# Command to start the FastAPI server using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]