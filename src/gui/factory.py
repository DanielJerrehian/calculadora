from customtkinter import CTk, CTkBaseClass

from src.gui.button import GuiButton
from src.gui.label import GuiLabel


class GuiFactory:
    padx = 0.5
    pady = 0.5
    sticky = "ew"

    def __init__(self, app: CTk) -> None:
        self.app = app

    def label(self, **kwargs) -> GuiLabel:
        return GuiLabel().create(app=self.app, **kwargs)

    def button(self, text, command, **kwargs) -> GuiButton:
        return GuiButton().create(app=self.app, text=text, command=command, **kwargs)

    def grid(self, component: CTkBaseClass, **kwargs) -> None:
        component.grid(**kwargs, padx=GuiFactory.padx, pady=GuiFactory.pady, sticky=GuiFactory.sticky)
