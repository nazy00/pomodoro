import tkinter as tk
from tkinter.ttk import Frame

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

        # --- render the frame --- #
        self.__container.mainloop()
