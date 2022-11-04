from typing import *
import socket
from ..AbstractClasses.AbstractBasicThreadTask import AbstractBasicThreadTask
from .modes_dictionary import modes
import struct
from .modes_dictionary import modes_dictionary


class RioSender:
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 12345

    def __init__(self):
        self.socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((RioSender.HOST, RioSender.PORT))        

    def send_mode(self, mode: modes, *args) -> None:
        self.socket.send(struct.pack("h", mode.value))
        self.socket.send(struct.pack(modes_dictionary[mode], *args))

    def send_volt_to_motor(self, id: int, volt: float) -> None: 
        self.send_mode(modes.setVolt, id, volt)
