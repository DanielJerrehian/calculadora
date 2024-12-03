from functools import reduce
from decimal import Decimal

from src.utils.operations import operations
from src.ui import UiController


class LogicController:
    def __init__(self, ui: UiController):
        self.ui = ui
        self.values = []
        self.operation = None
        self.concatenate = True
        self.answer = None
        self.last_input_was_operator = False

    def insert(self, value: str):
        self.last_input_was_operator = False
        current = self.ui.get()
        if value == "." and value in str(current) and self.concatenate:
            return
        text = f"{current}{value}" if self.concatenate else value
        self.concatenate = True
        self.ui.set(text=text)

    def calculate(self):
        self.concatenate = False
        if not self.operation:
            return
        self.values.append(Decimal(self.ui.get()))
        try:
            self.answer = reduce(operations[self.operation]["calculation"], self.values)
            self.ui.set(text=str(self.answer))
            self.values.clear()
        except ZeroDivisionError:
            self.ui.set(text="Error: Division by Zero")
            self.values.pop(len(self.values) - 1)
        self.operation = None
        self.last_input_was_operator = False

    def perform(self, operation: str):
        if self.last_input_was_operator:
            self.operation = operation
            self.last_input_was_operator = True
            return
        if self.operation:
            self.calculate()
        try:
            if self.ui.get():
                self.values.append(Decimal(self.ui.get()))
        except:
            self.values.append(self.answer)
        self.concatenate = False
        self.operation = operation
        self.last_input_was_operator = True
        if self.ui.get():
            self.ui.set(text=self.values[-1])

    def percentage(self):
        if not self.answer:
            try:
                self.answer = self.ui.get()
            except:
                return
        self.ui.set(text=f"{self.answer*100}%")

    # def negate(self):
    #     current = self.ui.get()
    #     if not current:
    #         self.insert(value="-")
    #         return
    #     inversion = Decimal(current) * -1
    #     self.ui.set(text=inversion)

    def restart(self) -> None:
        self.values.clear()
        self.operation = None
        self.concatenate = True
        self.answer = None
        self.last_input_was_operator = False
        self.ui.set(text="")
