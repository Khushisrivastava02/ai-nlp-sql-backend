from fastapi import FastAPI
from pydantic import BaseModel
import time

from app.nlp_to_sql import convert_question_to_sql
from app.sql_executor import execute_sql
from app.analytics import log_query, get_stats

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
def query(data: QueryRequest):

    start = time.time()

    sql = convert_question_to_sql(data.question)

    result = execute_sql(sql)

    execution_time = time.time() - start

    log_query(data.question, execution_time)

    return {
        "generated_sql": sql,
        "result": result,
        "execution_time": execution_time
    }

@app.get("/stats")
def stats():
    return get_stats()