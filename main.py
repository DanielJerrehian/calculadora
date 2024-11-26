from src.app import App
from src.gui.button import GuiButton
from src.gui.label import GuiLabel

from src.ui import UiController
from src.logic import LogicController
from src.utils.operations import operations


def main(title: str):
    app = App(title=title).create()
    label = GuiLabel().create(app=app)
    label.grid(row=0, column=0, columnspan=4, sticky="ew")
    ui = UiController(label=label)
    logic = LogicController(ui=ui)

    GuiButton().create(app=app, text=str(0), command=lambda: logic.insert(0)).grid(row=5, column=0, columnspan=2, padx=0.5, pady=0.5, sticky="ew")
    GuiButton().create(app=app, text=str("."), command=lambda: logic.insert(".")).grid(row=5, column=2, padx=0.5, pady=0.5)
    for index, digit in enumerate([7, 8, 9, 4, 5, 6, 1, 2, 3]):
        row = (index // 3) + 2
        column = index % 3
        button = GuiButton().create(app=app, text=str(digit), command=lambda value=digit: logic.insert(value))
        button.grid(row=row, column=column, padx=0.5, pady=0.5)

    for operation, attributes in operations.items():
        button = GuiButton().create(app=app, text=attributes["symbol"], command=lambda operation=operation: logic.perform(operation))
        button.grid(row=attributes["row"], column=3)

    GuiButton().create(app=app, text="Clear", command=logic.restart).grid(row=1, column=0, columnspan=3, padx=0.5, pady=0.5, sticky="ew")
    GuiButton().create(app=app, text="=", command=logic.calculate).grid(row=5, column=3, padx=0.5, pady=0.5)
    app.mainloop()


main(title="Calculator")
