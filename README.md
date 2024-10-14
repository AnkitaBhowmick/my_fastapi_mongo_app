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
   git clone https://github.com/your-username/fastapi_mongo_app.git


Insall the dependcies
    ```bash
    pip install -r requirements.txt

Running the application
    ```bash
    uvicorn app.main:app --reload

API Endpoints
Items API
Method	Endpoint	Description
POST	/items/	Create a new item.
GET	/items/{id}	Retrieve a specific item by ID.
GET	/items/filter	Filter items based on query parameters.
PUT	/items/{id}	Update an item’s details by ID.
DELETE	/items/{id}	Delete an item by ID.
GET	/items/aggregate/count	Count items grouped by email (aggregation).
Clock-In API
Method	Endpoint	Description
POST	/clock-in/	Create a new clock-in record.
GET	/clock-in/{id}	Retrieve a clock-in record by ID.
GET	/clock-in/filter	Filter clock-in records by query params.
PUT	/clock-in/{id}	Update a clock-in record by ID.
DELETE	/clock-in/{id}	Delete a clock-in record by ID.
Environment Variables
Create a .env file in the root of your project to store environment variables:

bash
Copy code
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority
SECRET_KEY=your-secret-key
MONGO_URI: MongoDB connection string.
SECRET_KEY: Secret key for JWT tokens or other security purposes.
Deploying on Koyeb
Create a Procfile in the root directory:

bash
Copy code
web: uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-5000}
Push your code to a GitHub repository.

Go to the Koyeb Dashboard and create a new service, connecting your GitHub repository.

Choose the branch to deploy and click Create Service. Koyeb will automatically detect the Procfile.

Once deployed, you can access the API via the provided Koyeb URL.

Author-
Ankita Bhowmick
