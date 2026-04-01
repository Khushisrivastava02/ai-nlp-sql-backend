# AI NLP to SQL Backend

A FastAPI backend that converts natural language questions into SQL queries and executes them on a SQLite database. This project allows non-technical users to ask questions like:

"How many students enrolled in Python courses in 2024?"

Example:  
User Question → "Show all students"  
Generated SQL → SELECT * FROM students LIMIT 5

---

## Features

- Convert natural language to SQL queries  
- Execute SQL queries on database  
- FastAPI REST API  
- Query execution analytics (total queries, common keywords, slowest queries)  
- Unit testing with Pytest  
- Docker containerization (optional Kubernetes deployment)

---

## Tech Stack

- Python  
- FastAPI  
- SQLite  
- Pytest  
- Uvicorn  
- Docker  
- Kubernetes (optional)

---

## Project Structure

```
ai-nlp-sql-backend/
│
├── app/
│   ├── main.py
│   ├── nlp_to_sql.py
│   ├── sql_executor.py
│   └── analytics.py
│
├── tests/
│   └── test_api.py
│
├── screenshots/
│   ├── api_running.png
│   └── query_output.png
│
├── requirements.txt
├── Dockerfile
├── nlp2sql_pod.yaml
├── nlp2sql_service.yaml
└── README.md
```

---

## Installation

Clone the repository

```
git clone https://github.com/Khushisrivastava02/ai-nlp-sql-backend.git
cd ai-nlp-sql-backend
```

Create a virtual environment

```
python -m venv venv
```

Activate environment (Windows)

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

## Run the API

Start the FastAPI server

```
uvicorn app.main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

API Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Docker Setup

Build the Docker image

```
docker build -t nlp2sql_app:latest .
```

Run the container

```
docker run -d -p 8000:8000 --name nlp2sql_container nlp2sql_app:latest
```

Access API

```
http://localhost:8000/docs
```

Stop container

```
docker stop nlp2sql_container
docker rm nlp2sql_container
```

---

## Optional Kubernetes Deployment

Deploy using YAML files

```
kubectl apply -f nlp2sql_pod.yaml
kubectl apply -f nlp2sql_service.yaml
kubectl get pods
kubectl get svc
```

Access API

```
http://localhost:30080/docs
```

---

## API Example

### POST /query

Request Body

```
{
  "question": "Show all students"
}
```

Response

```
{
  "generated_sql": "SELECT * FROM students LIMIT 5",
  "result": [...],
  "execution_time": 0.01
}
```

### GET /stats

Returns total queries, most common keywords, and slowest query.

---

## Testing

Run tests using

```
pytest
```

---

## Screenshots

### API Running

![API Running](screenshots/api_running.png)

### Query Output

![Query Result](screenshots/query_output.png)

---

## GitHub Instructions

To push updates

```
git add .
git commit -m "Update README and add Docker setup"
git push
```

---

## Author

Khushi Srivastava  
B.Tech CSE