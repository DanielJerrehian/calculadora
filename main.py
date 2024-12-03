from src.app import App
from src.gui.factory import GuiFactory
from src.ui import UiController
from src.logic import LogicController
from src.utils.operations import operations


def main(title: str):
    app = App(title=title).create()
    factory = GuiFactory(app=app)
    label = factory.label()
    factory.grid(component=label, **{"row": 0, "column": 0, "columnspan": 4})
    ui = UiController(label=label)
    logic = LogicController(ui=ui)

    clear = factory.button(text="Clear", command=logic.restart)
    factory.grid(component=clear, **{"row": 1, "column": 0, "columnspan": 2})

    # negative = factory.button(text="±", command=logic.negate)
    # factory.grid(component=negative, **{"row": 1, "column": 1})

    percentage = factory.button(text="%", command=logic.percentage)
    factory.grid(component=percentage, **{"row": 1, "column": 2})

    for index, digit in enumerate([7, 8, 9, 4, 5, 6, 1, 2, 3]):
        button = factory.button(text=str(digit), command=lambda value=digit: logic.insert(value))
        factory.grid(component=button, **{"row": (index // 3) + 2, "column": index % 3})

    for operation, attributes in operations.items():
        button = factory.button(text=attributes["symbol"], command=lambda operation=operation: logic.perform(operation))
        factory.grid(component=button, **{"row": attributes["row"], "column": 3})

    zero = factory.button(text=str(0), command=lambda: logic.insert(0))
    factory.grid(component=zero, **{"row": 5, "column": 0, "columnspan": 2})

    decimal = factory.button(text=str("."), command=lambda: logic.insert("."))
    factory.grid(component=decimal, **{"row": 5, "column": 2})

    equals = factory.button(text="=", command=logic.calculate)
    factory.grid(component=equals, **{"row": 5, "column": 3})

    app.mainloop()


if __name__ == "__main__":
    main(title="Calculator")
