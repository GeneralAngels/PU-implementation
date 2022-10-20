import struct
from typing import *

class RobotState:
    FMT: str = "ff"

    def __init__(self, angle: float, distance: float) -> None:
        self.angle = angle
        self.distance = distance

    @staticmethod
    def unpack(_recv) -> 'RobotState':
        return struct.unpack(RobotState.FMT, _recv)
