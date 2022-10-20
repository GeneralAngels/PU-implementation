from Components.TaskManager import TaskManager
from Components.RioReciever.RioReciever import RioReciever
from Components.RioSender.RioSender import RioSender
import time


task_manager: TaskManager = TaskManager()
task_manager.schedule(RioReciever())
time.sleep(1)
print(task_manager.tasks_list)
input("stop?")