# my_fastapi_mongo_app

# FastAPI MongoDB CRUD Application

This is a REST API built with **FastAPI** and **MongoDB** that supports CRUD operations for managing items and user clock-in records. The project uses MongoDB for data storage and provides endpoints to create, retrieve, update, and delete records.

## Features

1. **Items API**:
   - Create, Read, Update, and Delete (CRUD) operations for managing items.
   - Filtering of items by various fields (email, expiry date, etc.).
   - Aggregation to count items per email.

2. **Clock-In Records API**:
   - CRUD operations for managing user clock-in records.
   - Filtering clock-in records based on email, location, and time.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
  - [Items API](#items-api)
  - [Clock-In API](#clock-in-api)
- [Environment Variables](#environment-variables)
- [Deploying on Koyeb](#deploying-on-koyeb)
- [Deploying on Heroku](#deploying-on-heroku)

## Tech Stack

- **FastAPI**: The web framework.
- **MongoDB**: The database for storing items and clock-in records.
- **Pydantic**: Data validation and settings management.
- **Uvicorn**: ASGI server to serve the application.
- **HTML/CSS/JS**: For the front-end of the application.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AnkitaBhowmick/fastapi_mongo_app.git


Insall the dependcies
    ```bash
    pip install -r requirements.txt

Running the application
    ```bash
    uvicorn app.main:app --reload


Author-
Ankita Bhowmick
