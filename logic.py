from customtkinter import CTkLabel
from functools import reduce
from decimal import Decimal

from operations import operations


class Logic:
    def __init__(self, label: CTkLabel):
        self.label = label
        self.values = []
        self.length = len(self.values)
        self.operation = None
        self.concatenate = True
        self.answer = None
        self.last_input_was_operator = False

    def insert(self, value: str):
        self.last_input_was_operator = False
        current = self.label.cget("text")
        if value == "." and value in str(current) and self.concatenate:
            return
        text = f"{current}{value}" if self.concatenate else value
        self.concatenate = True
        self.label.configure(text=text)

    def restart(self) -> None:
        self.values.clear()
        self.length = len(self.values)
        self.operation = None
        self.concatenate = True
        self.answer = None
        self.last_input_was_operator = False
        self.label.configure(text="")

    def perform(self, operation: str):
        if self.last_input_was_operator:
            self.operation = operation
            self.last_input_was_operator = True
            return
        if self.operation:
            self.calculate()
        try:
            self.values.append(Decimal(self.label.cget("text")))
            self.length = len(self.values)
        except ValueError:
            self.values.append(self.answer)
        self.concatenate = False
        self.operation = operation
        self.last_input_was_operator = True
        self.label.configure(text=self.values[-1])

    def calculate(self):
        self.concatenate = False
        self.values.append(Decimal(self.label.cget("text")))
        self.length = len(self.values)
        if not self.operation:
            return
        try:
            self.answer = reduce(operations[self.operation]["calculation"], self.values)
            self.label.configure(text=str(self.answer))
        except ZeroDivisionError:
            self.label.configure(text="Error: Division by Zero")
            self.values.pop(len(self.values) - 1)
            self.length = len(self.values)
        self.values.clear()
        self.length = len(self.values)
        self.operation = None
        self.last_input_was_operator = False
