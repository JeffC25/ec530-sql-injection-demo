# Use the Python 3.9 slim image as the base
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY ./api/** ./api/
COPY ./templates/** ./templates/
COPY ./app.py .
COPY ./init_data.py .
COPY ./users.csv .
COPY gunicorn.conf.py .

# Set the FLASK_APP environment variable
ENV FLASK_APP=app.py

# Expose port 5000 for the Flask application
EXPOSE 5000

# Run the data initialization script
RUN python init_data.py

# Run the Flask application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]
