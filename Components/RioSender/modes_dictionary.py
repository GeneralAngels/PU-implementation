from enum import Enum
from typing import *

class modes(Enum):
    setVolt = 0

modes_dictionary: Dict[Enum, str] = {
    modes.setVolt: "f" # motor id, voltage
}