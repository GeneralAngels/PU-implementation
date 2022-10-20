import struct
from typing import *
from ..AbstractClasses.AbstractBasicThreadTask import AbstractBasicThreadTask
from .RobotState import RobotState
import socket
import time


class RioReciever(AbstractBasicThreadTask):
    HOST = socket.gethostbyname(socket.gethostname())
    HOST = "127.0.0.1"
    PORT = 65432
    
    def __init__(self) -> None:
        self.last_robot_state: RobotState
        self.socket: socket.socket

    def start(self) -> None:
        self.socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((RioReciever.HOST, RioReciever.PORT))
        self.socket.listen()
        self.conn, self.addr = self.socket.accept()
        
    def execute(self) -> None:
        self.last_robot_state: RobotState = RobotState.unpack(self.conn.recv(struct.calcsize(RobotState.FMT)))
        print(self.last_robot_state.angle, self.last_robot_state.distance)

    def end(self) -> None:
        self.socket.close()

    def isFinished(self) -> None:
        return False