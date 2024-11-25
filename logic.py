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

    def insert(self, digit: int):
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

    def perform(self, operation: str):
        if self.operation:
            self.calculate()
        self.operation = operation
        if len(self.values) == self.length:
            try:
                self.values.append(int(self.label.cget("text")))
                self.length = len(self.values)
            except ValueError:
                self.values.append(self.answer)
            self.concatenate = False
            self.label.configure(text="")
            self.label.configure(text=self.values[len(self.values) - 1])

    def calculate(self):
        self.concatenate = False
        self.values.append(int(self.label.cget("text")))
        self.length = len(self.values)
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
