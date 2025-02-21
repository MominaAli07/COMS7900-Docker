# Use a base Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy all project files (including templates/)
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose Flask port
EXPOSE 5001

# Run Flask app
CMD ["python", "app.py"]

