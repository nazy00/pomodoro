import tkinter as tk
from tkinter.ttk import Frame
from .pomodoro import Pomodoro

# map of constants
CONST = {
    "win-title": "Study Timer",
    "win-width": 450,
    "win-height": 200,
}


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title(str(CONST["win-title"]))
        self.geometry(f"{CONST['win-width']}x{CONST['win-height']}")
        self.resizable(False, False)


class AppFrame(Frame):
    def __init__(self, container: tk.Tk = App()):
        self.__container = container
        super().__init__(self.__container)

        # TODO: create UI elements
        self.__container.grid_rowconfigure(0, weight=4)
        self.__container.grid_rowconfigure(1, weight=1)

        self.__container.grid_columnconfigure(0, weight=2)
        self.__container.grid_columnconfigure(1, weight=1)
        self.__container.grid_columnconfigure(2, weight=1)

        self.__pomodoro = Pomodoro()
        # self.__time_label = tk.Label(self.__container, text="30:00")
        self.__time_label = tk.Label(self.__container, text=self.__pomodoro.time)
        self.__time_label.grid(row=0, column=0, columnspan=3)

        self.__state_label = tk.Label(self.__container, text=self.__pomodoro.state)
        self.__state_label.grid(row=1, column=0)

        self.__start_button = tk.Button(
            self.__container, text="Start", command=self.__pomodoro.start
        )
        self.__start_button.grid(row=2, column=2)

        self.__reset_button = tk.Button(
            self.__container, text="Reset", command=self.__pomodoro.reset
        )
        self.__reset_button.grid(row=2, column=3)

        self.after(1000, self.update)

        # self.__pomodoro.start()
        # self.__time_label.config(text=self.__pomodoro.time)

        # --- render the frame --- #
        self.__container.mainloop()

    def update(self) -> None:
        self.__time_label.config(text=self.__pomodoro.time)
        self.__state_label.config(text=self.__pomodoro.state)
        self.after(1000, self.update)
