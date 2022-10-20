from typing import *
import threading
from .AbstractClasses.AbstractBasicThreadTask import SimpleTask
from .AbstractClasses.AbstractThreadTask import AbstractThreadTask
import time


class TaskManager:
    def __init__(self):
        self.tasks_list: List[AbstractThreadTask] = []

    def schedule(self, task: AbstractThreadTask) -> None:
        task._thread: threading.Thread = threading.Thread(target=task.get_thread_function(), args=())
        task._thread.start()
        self.tasks_list.append(task)

    def cancel_task(self, task: AbstractThreadTask) -> None:
        task._thread.terminate()
        self.tasks_list.remove(task)


task_manager: TaskManager = TaskManager()
task_manager.schedule(SimpleTask(1))
task_manager.schedule(SimpleTask(2))
time.sleep(10)