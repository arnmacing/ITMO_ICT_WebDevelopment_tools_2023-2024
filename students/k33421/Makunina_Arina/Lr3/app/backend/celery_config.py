import sys

from celery import Celery
import os

print("Current working directory:", os.getcwd())
print("Python path:", sys.path)

REDIS_URL = os.getenv("REDIS_URL")
celery_app = Celery("backend", broker=REDIS_URL, backend=REDIS_URL)


@celery_app.task
def example_task(data):
    return f"Processed {data}"
