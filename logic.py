from customtkinter import CTkLabel
from functools import reduce

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

    def insert(self, digit: int):
        self.last_input_was_operator = False
        if self.concatenate:
            current = self.label.cget("text")
            number = f"{current}{digit}"
            self.label.configure(text=number)
        else:
            self.concatenate = True
            self.label.configure(text=digit)

    def restart(self) -> None:
        self.values.clear()
        self.operation = None
        self.length = len(self.values)
        self.label.configure(text="")
        self.last_input_was_operator = False

    def perform(self, operation: str):
        if not self.last_input_was_operator:
            if self.operation:
                self.calculate()
            try:
                self.values.append(int(self.label.cget("text")))
                self.length = len(self.values)
            except ValueError:
                self.values.append(self.answer)
            self.concatenate = False
            self.label.configure(text=self.values[-1])
        self.operation = operation
        self.last_input_was_operator = True

    def calculate(self):
        self.concatenate = False
        self.values.append(int(self.label.cget("text")))
        self.length = len(self.values)
        if self.operation:
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
