from pytest import fixture
from unittest.mock import MagicMock, patch


@fixture()
def mock():
    return MagicMock()


@fixture
def button():
    with patch("src.gui.button.CTkButton") as MockCTkButton:
        yield MockCTkButton


@fixture
def label():
    with patch("src.gui.label.CTkLabel") as MockCTkLabel:
        yield MockCTkLabel
