# Use the official Python image as a base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the entire current directory into the container at /app
COPY . /app

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 to the outside world
EXPOSE 8080

# Define environment variable PORT
ENV PORT 8080

# Make the bash script executable
RUN chmod +x ./run.sh

# Command to run the bash script
CMD ["./run.sh"]