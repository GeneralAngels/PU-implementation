from typing import *
from abc import ABC
import time
from AbstractClasses.AbstractThreadTask import AbstractThreadTask
from AbstractClasses.AbstractTask import AbstractTask


class AbstractBasicThreadTask(AbstractThreadTask, AbstractTask):
    def get_thread_function(self) -> callable:
        def _func():
            self.start()
            while not self.isFinished():
                self.execute()
            self.end()
        return _func


class SimpleTask(AbstractBasicThreadTask):    
    def __init__(self, id: int) -> None:
        self.id = id
    
    def start(self) -> None:
        self.start_time: float = time.time()

    def execute(self) -> None:
        time.sleep(0.5)
        print("Another run:", self.id)

    def end(self) -> None:
        print("finished run:", self.id)

    def isFinished(self) -> None:
        return time.time() - self.start_time >= 5