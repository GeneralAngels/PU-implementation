from abc import ABC, abstractmethod
from typing import *


class AbstractTask(ABC):
    @abstractmethod
    def start(self) -> None: raise NotImplementedError

    @abstractmethod
    def execute(self) -> None: raise NotImplementedError

    @abstractmethod
    def isFinished(self) -> None: raise NotImplementedError

    @abstractmethod
    def end(self) -> None: raise NotImplementedError

