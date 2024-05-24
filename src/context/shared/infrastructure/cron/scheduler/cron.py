from typing import Any
from apscheduler.schedulers.background import BackgroundScheduler

class Time():
  def __init__(self, hour: int, minutes: int):
    self.hour = hour
    self.minutes = minutes

class Cron():
  def __init__(self, time: Time):
    self.time = time
    
  def initialize_cron(self,job: Any):
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'cron', hour=14, minute=0)
    scheduler.start()
