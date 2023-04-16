from time import sleep
from datetime import timedelta


class Timer:
    def __init__(self, minutes: int = 0, seconds: int = 0):
        self.total_seconds = seconds + minutes * 60
        self.__STOP = False

    def __str__(self) -> str:
        return str(timedelta(seconds=self.total_seconds))[2:]

    @property
    def time(self) -> int:
        return str(self)

    def start(self):
        while self.total_seconds > 0:
            if self.__STOP:
                self.total_seconds = 0
                break
            sleep(1)
            self.total_seconds -= 1

    def stop(self):
        self.__STOP = True
