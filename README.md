# Flask Calculator App

This repository contains a Flask-based calculator application that can be deployed using Docker or Singularity (Apptainer).

## Docker Compose Setup

A `docker-compose.yml` file is provided to set up your application container using the image hosted on Docker Hub.

```yaml
version: "3.8"

services:
  flask-app:
    image: momina07/flask-calculator:latest  # Using our Docker Hub image
    ports:
      - "8082:5001"
    volumes:
      - .:/app
    environment:
      - FLASK_ENV=development
    restart: always  # Automatically restarts the container if it stops
```

To build and run the container, execute the following command in your terminal:

```bash
docker-compose up --d
```

## Docker Hub Container

The Docker image is hosted on Docker Hub. You can pull the image directly from the following URL:

[Docker Hub: momina07/flask-calculator](https://hub.docker.com/r/momina07/flask-calculator)

## Singularity Image File (SIF)

If you have converted your Docker image into a Singularity Image File (SIF), you can download it using the link below:

[SIF File Download](https://mtmailmtsu-my.sharepoint.com/:u:/g/personal/yz3r_mtmail_mtsu_edu/Edoo23CyqZ5Nvj4PwPrLycMB0_T1dPTvHfJqTmXf15o6kQ?e=VFFb7f)

To run the application using Apptainer (formerly Singularity), use the command:

```bash
apptainer exec flask-calculator.sif python3 /app/app.py
```

## How It Works Together

- **Docker Compose:** Running `docker-compose up --build` pulls the Docker image (if needed), builds the container, and runs your Flask app.
- **Docker Hub:** The image on Docker Hub serves as the source for the Docker container. Anyone can pull and run this image using Docker.
- **Singularity (Apptainer):** The SIF file allows you to run the containerized application using Apptainer, providing an alternative to Docker.


