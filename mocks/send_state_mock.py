from typing import *
import struct
import socket


class SendStateMock:
    STRUCT_FMT = "ff"
    
    def __init__(self, host: str, port: int):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        print("connected")
        
    def send(self):
        self.socket.send(struct.pack(SendStateMock.STRUCT_FMT, 2, 3))