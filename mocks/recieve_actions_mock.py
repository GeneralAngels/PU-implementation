from typing import *
import struct
import socket
from ..Components.RioSender.modes_dictionary import modes_dictionary

class RecieveActionsMock:
    FMT = "f"
    def __init__(self, host: str, port: int):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        print("connected")
        
    def recieve(self):
        mode = self.socket.recv(2)
        voltage = struct.unpack(self.FMT, self.socket.recv(struct.calcsize(self.FMT)))
        print(f"mode: {mode}, voltage: {voltage}")