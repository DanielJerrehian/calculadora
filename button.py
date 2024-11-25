from customtkinter import CTkButton, CTk
from collections.abc import Callable


class GuiButton:
    def __init__(self):
        pass

    def create(self, app: CTk, text: str, command: Callable, **kwargs) -> CTkButton:
        return CTkButton(master=app, text=text, command=command, font=("Arial", 18), corner_radius=0, width=80, **kwargs)
