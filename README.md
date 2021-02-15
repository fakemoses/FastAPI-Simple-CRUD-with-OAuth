#A simple CRUD API with OAuth using FastAPI

This project served as a simple multi platform Information system used personally by me. 

## Requirements

A mongodb is required and a user database with user_collections is manually created. Following informations are required:

```
  "email": "your preferences",
  "password": "your pass"
```

## How to use

Run the following command:
```
pip install requirements.txt
```

Create a .env file and add 3 parameters below:
```
MONGO_URI
JWT_SECRET
JWT_ALGO
```
or you can change directly from the file itself.

I personally run this in heroku. 
