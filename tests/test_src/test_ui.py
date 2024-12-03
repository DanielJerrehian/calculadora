from src.ui import UiController


def test_class_exists():
    assert UiController


def test_constructor(mock):
    ui = UiController(label=mock)
    assert ui.label == mock


def test_get(mock):
    value = "Test Value"
    mock.cget.return_value = value
    ui = UiController(label=mock)
    text = ui.get()
    mock.cget.assert_called_once_with("text")
    assert text == value


def test_set(mock):
    value = "New Value"
    ui = UiController(label=mock)
    ui.set(text=value)
    mock.configure.assert_called_once_with(text=value)
