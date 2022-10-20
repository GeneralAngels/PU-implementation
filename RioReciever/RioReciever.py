import struct
from typing import *
from AbstractClasses.AbstractBasicThreadTask import AbstractBasicThreadTask
from RioReciever.RobotState import RobotState
import socket


class RioReciever(AbstractBasicThreadTask):
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 56789
    
    def __init__(self) -> None:
        self.last_robot_state: RobotState
        self.socket: socket.socket

    def start(self) -> None:
        self.socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((RioReciever.HOST, RioReciever.PORT))

    def execute(self) -> None:
        self.last_robot_state: RobotState = RobotState.unpack(self.socket.recv(struct.calcsize(RobotState.FMT)))

    def end(self) -> None:
        self.socket.close()

    def isFinished(self) -> None:
        return False