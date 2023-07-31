# Base image
FROM python:3.9
# Set the working directory inside the container
WORKDIR /inventory

# Copy the FastAPI app file to the container's working directory

COPY ./requirements.txt /inventory/requirements.txt
# Install required dependencies
RUN pip install --no-cache-dir --upgrade -r /inventory/requirements.txt
RUN  python3 -m .portcheck
RUN  python3 -m .sshcomm
COPY app ./
# Expose the port that FastAPI will be running on
EXPOSE 80

# Command to start the FastAPI server using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]