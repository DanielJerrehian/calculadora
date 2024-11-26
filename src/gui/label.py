from customtkinter import CTkLabel, CTk


class GuiLabel:
    def __init__(self):
        pass

    def create(self, app: CTk, text: str = "", **kwargs) -> CTkLabel:
        return CTkLabel(master=app, text=text, height=50, font=("Arial", 24), padx=2, pady=2, **kwargs)
