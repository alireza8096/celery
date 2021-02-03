from celery import Celery

app = Celery('sms_sender', broker='pyamqp://guest@localhost//')


@app.task
def add(x, y):
    return x + y
