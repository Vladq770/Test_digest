from celery import shared_task
import requests


@shared_task()
def task_create_digest(params):
    response = requests.post('http://backend:7000/digest/createdigest/', params=params)
    return response.json(), response.status_code
