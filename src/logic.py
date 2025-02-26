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
            formatted = self._format(text=f"{self.answer:.8f}") if len(str(self.answer)) >= 8 else self._format(text=f"{self.answer}")
            self.ui.set(text=formatted)
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
            self.ui.set(text=str(self.values[-1]))

    def percentage(self):
        if not self.answer:
            try:
                self.answer = Decimal(self.ui.get())
            except:
                return
        self.ui.set(text=f"{self.answer*100}%")

    def restart(self) -> None:
        self.values.clear()
        self.operation = None
        self.concatenate = True
        self.answer = None
        self.last_input_was_operator = False
        self.ui.set(text="")

    def _format(self, text: str) -> str:
        if "." not in text:
            return text
        values = text.split(".")
        integer = values[0]
        decimal = list(values[1])[::-1]
        count = 0
        for character in decimal:
            if character == "0":
                count = count + 1
            else:
                break
        decimal = "".join(decimal[count:][::-1])
        text = f"{integer}.{decimal}" if decimal else integer
        return text
