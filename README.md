# JokeAPI

## Overview
This project is a simple Flask-based web application that serves a collection of jokes. It's a lightweight and fun project, ideal for understanding the basics of web APIs and Flask framework.

## Features
- **Random Jokes:** The API randomly selects jokes from a predefined list.
- **Customizable:** Users can request a specific number of jokes.

## How to Run
This application is containerized using Docker, making it easy to build and run.

### Prerequisites
- Docker
- Python 3.10

### Running the Application
1. **Build the Docker Image:**
   ```bash
   docker build -t joke-api .
1. **Run Container**
docker run -p 5000:5000 joke-api
