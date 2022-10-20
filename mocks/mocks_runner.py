from send_state_mock import SendStateMock
import time


mock = SendStateMock("127.0.0.1", 65432)
while True:
    mock.send()
    time.sleep(0.2)