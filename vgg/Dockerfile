# Use the official Python image from Docker Hub
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt into the container at /app
COPY requirements.txt .

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .
RUN mkdir -p /app/uploads


# Expose the port that the Flask app will run on
EXPOSE 5001

# Command to run the Flask app
CMD ["python", "app.py"]
