from unittest.mock import MagicMock

from src.gui.factory import GuiFactory


def test_class_exists():
    assert GuiFactory


def test_constructor(mock):
    factory = GuiFactory(app=mock)
    assert factory.app


def test_label(mock, label):
    factory = GuiFactory(app=mock)
    result = factory.label()
    label.assert_called_once()
    assert result is label.return_value


def test_button(mock, button):
    factory = GuiFactory(app=mock)
    text = "Button"
    command = lambda: 5 + 10
    result = factory.button(text=text, command=command)
    button.assert_called_once()
    assert result is button.return_value


def test_grid(mock):
    factory = GuiFactory(app=mock)
    component = MagicMock()
    factory.grid(component=component, row=0, column=0)
    component.grid.assert_called_once_with(row=0, column=0, padx=GuiFactory.padx, pady=GuiFactory.pady, sticky=GuiFactory.sticky)
