from fastapi import FastAPI, BackgroundTasks
from celery.result import AsyncResult

from tasks import parse_url_task
from celery_config import celery_app

app = FastAPI()


@app.post("/parse/")
async def parse_url(url: str):
    task = parse_url_task.delay(url)
    return {"task_id": task.id}


@app.get("/result/{task_id}")
def get_result(task_id: str):
    result = AsyncResult(task_id, app=celery_app)
    if result.state == "SUCCESS":
        return {"status": result.state, "result": result.result}
    return {"status": result.state}
