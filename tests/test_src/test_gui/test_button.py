from src.gui.button import GuiButton


def test_class_exists():
    assert GuiButton


def test_constructor():
    instance = GuiButton()
    assert instance


def test_create(mock, button):
    instance = GuiButton()
    text = "Button"
    command = lambda: 5 + 10
    result = instance.create(app=mock, text=text, command=command)
    button.assert_called_once_with(master=mock, text=text, command=command, font=("Arial", 18), corner_radius=0, width=80)
    assert result is button.return_value
