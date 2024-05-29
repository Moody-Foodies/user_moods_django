# User Mood Api
- This project was developed during Mod 4 Hackaton in under 6 hours. This project have the purpose of serving as a microservice to Brain Food Organization in the second stretch of Capstone Project. This API have two endpoints, one to retrieve all user moods and one to create new instances of Mood for an user.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Server](#running-the-server)
- [Running Tests](#running-tests)
- [API Endpoints](#api-endpoints)
  - [Get Moods](#get-moods)
  - [Post Mood](#post-mood)

## Prerequisites
- Python 3.12.3
- pip, version 24.0
- PostgreSQL
- virtualenv

## Installation
- Clone the Repository
```Bash
git clone <repository_url>
```

- Navigate to the project directory:
```Bash
cd django_mood_api
```

- Create a virtual environment:
```Bash
python3 -m venv venv
```

- Activate the virtual environment:
  - On macOS/Linux:
```Bash
source venv/bin/activate
```
  - On Windows:
```Bash
venv\scripts\activate
```

- Install the dependencies:
```Bash
pip install -r requirements.txt
```

- Set up environments variables:
  - Create a `.env` file in the project root and add the following:
```Bash
DJANGO_SECRET_KEY=your-very-secret-key
```

- Apply migrations:
```Bash
python manage.py migrate
```

## Running the Server
1) Start the development server:
```Bash
python manage.py runserver
```
2) Open your browser and navigate to `http://127.0.0.1:8000`.

## Running Tests
```Bash
python manage.py test
```

## API Endpoints
### Get Moods

**URL:** `/api/moods/`

**Method:** `GET`

**Query Parameters:**

- `user_id` (required): The ID of the user to get moods for.

**Response:**

```json
{
  "data": {
    "id": "1",
    "type": "moods",
    "attributes": {
      "avg_mood": 3.5,
      "user_moods": [
        {"date": "2024-05-01", "mood": 4},
        {"date": "2024-05-02", "mood": 3}
      ]
    }
  }
}
```
**Example Request:**
```Bash 
GET "http://127.0.0.1:8000/api/moods/?user_id=1"
```

### Post Mood

**URL:** `/api/moods/`

**Method:** `POST`

**Request Body:**

```json
{
  "user_id": 1,
  "mood": 4
}

```
**Response:**
```json 
{
  "user_id": 1,
  "mood": 4,
  "date": "2024-05-23"
}
```
**Example Request:**
```Bash
curl -X POST "http://127.0.0.1:8000/api/moods/" -H "Content-Type: application/json" -d '{"user_id": 1, "mood": 4}'
```

