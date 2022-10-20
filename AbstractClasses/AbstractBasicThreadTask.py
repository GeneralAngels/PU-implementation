from typing import *
from abc import ABC

from AbstractClasses.AbstractThreadTask import AbstractThreadTask
from AbstractClasses.AbstractTask import AbstractTask


class AbstractBasicThreadTask(AbstractThreadTask, AbstractTask):
    def get_thread_function(self) -> callable:
        self.start()
        while not self.isFinished():
            self.execute()
        self.end()