from app import App
from button import GuiButton
from label import GuiLabel
from logic import Logic
from operations import operations


def main(title: str):
    app = App(title=title).create()
    label = GuiLabel().create(app=app)
    label.grid(row=0, column=0, columnspan=4, sticky="ew")
    logic = Logic(label=label)

    GuiButton().create(app=app, text=str(0), command=lambda: logic.insert(0)).grid(row=5, column=0, columnspan=3, padx=0.5, pady=0.5, sticky="ew")
    for index, digit in enumerate([7, 8, 9, 4, 5, 6, 1, 2, 3]):
        row = (index // 3) + 2
        column = index % 3
        button = GuiButton().create(app=app, text=str(digit), command=lambda digit=digit: logic.insert(digit))
        button.grid(row=row, column=column, padx=0.5, pady=0.5)

    for operation, attributes in operations.items():
        button = GuiButton().create(app=app, text=attributes["symbol"], command=lambda operation=operation: logic.perform(operation))
        button.grid(row=attributes["row"], column=3)

    GuiButton().create(app=app, text="Clear", command=logic.restart).grid(row=1, column=0, columnspan=3, padx=0.5, pady=0.5, sticky="ew")
    GuiButton().create(app=app, text="=", command=logic.calculate).grid(row=5, column=3, padx=0.5, pady=0.5)
    app.mainloop()


main(title="Calculator")
