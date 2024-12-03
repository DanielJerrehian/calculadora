from src.gui.label import GuiLabel


def test_class_exists():
    assert GuiLabel


def test_constructor():
    instance = GuiLabel()
    assert instance


def test_create(mock, label):
    instance = GuiLabel()
    result = instance.create(app=mock)
    label.assert_called_once()
    assert result is label.return_value
