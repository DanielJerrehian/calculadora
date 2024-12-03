from customtkinter import CTk

from src.app import App


def test_class_exists():
    assert App


def test_constructor():
    title = "My App"
    instance = App(title=title)
    assert instance.title == title


def test_app_create():
    title = "My App"
    instance = App(title=title)
    app = instance.create()
    assert isinstance(app, CTk)
    assert app.title() == title
