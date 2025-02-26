from customtkinter import CTkLabel


class UiController:
    def __init__(self, label: CTkLabel):
        self.label = label

    def get(self) -> str:
        return self.label.cget("text")

    def set(self, text: str):
        self.label.configure(text=text)
