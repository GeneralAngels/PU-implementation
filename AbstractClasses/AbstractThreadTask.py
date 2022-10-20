from typing import *
from abc import ABC, abstractmethod


class AbstractThreadTask(ABC):
    @abstractmethod
    def get_thread_function(self) -> callable:
        raise NotImplementedError