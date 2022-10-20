from concurrent.futures import thread
from typing import *
import threading
from AbstractClasses.AbstractThreadTask import AbstractThreadTask


class TaskManager:
    def __init__(self):
        self.tasks_list: List[AbstractThreadTask] = []

    def schedule(self, task: AbstractThreadTask) -> None:
        task._thread: threading.Thread = threading.Thread(target=task.get_thread_function(task), args=())
        task._thread.start()
        self.tasks_list.append(task)

    def cancel_task(self, task: AbstractThreadTask) -> None:
        task._thread.terminate()
