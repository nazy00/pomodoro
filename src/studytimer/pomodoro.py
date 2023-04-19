from .timer import Timer
from tkinter import Label


class Pomodoro:
    def __init__(self) -> None:
        self.__STATES = ("work", "short break", "long break")
        self.state = self.__STATES[0]
        self.work_timer = Timer(minutes=30)
        self.__STOP = False

    def __str__(self) -> str:
        if self.state == self.__STATES[0]:
            current_timer = self.work_timer
        elif self.state == self.__STATES[1]:
            current_timer = self.short_break_timer
        else:
            current_timer = self.long_break_timer
        return current_timer.time

    @property
    def time(self) -> int:
        return str(self)

    def start(self):
        count = 1
        while not self.__STOP:
            self.work_timer.start()

            if count % 4:
                self.state = self.__STATES[1]
                self.short_break_timer = Timer(minutes=10)
                self.short_break_timer.start()
            else:
                self.state = self.__STATES[2]
                self.long_break_timer = Timer(minutes=20)
                self.long_break_timer.start()

            count += 1
            self.state = self.__STATES[0]
            self.work_timer = Timer(minutes=30)

    def reset(self):
        if not self.__STOP:
            self.__STOP = True
            if self.state == self.__STATES[0]:
                self.work_timer.stop()
            elif self.state == self.__STATES[1]:
                self.short_break_timer.stop()
            elif self.state == self.__STATES[2]:
                self.long_break_timer.stop()
