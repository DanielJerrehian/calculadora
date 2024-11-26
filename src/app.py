from customtkinter import CTk


class App:
    def __init__(self, title: str) -> None:
        self.title = title

    def create(self) -> CTk:
        app = CTk()
        app.title(self.title)
        return app
