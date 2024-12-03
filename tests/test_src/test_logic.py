from unittest.mock import MagicMock
from decimal import Decimal

from src.logic import LogicController


def test_class_exists():
    assert LogicController


def test_constructor(mock):
    logic = LogicController(ui=mock)
    assert logic.ui == mock
    assert logic.values == []
    assert logic.operation == None
    assert logic.concatenate
    assert logic.answer == None
    assert logic.last_input_was_operator == False


def test_insert(mock):
    mock.get.return_value = 4
    logic = LogicController(ui=mock)
    logic.insert(value=".5")
    mock.set.assert_called_once_with(text="4.5")
    mock.get.return_value = "4.5"
    assert logic.ui.get() == "4.5"


def test_insert_double_decimal_point(mock):
    mock.get.return_value = "1.0"
    logic = LogicController(ui=mock)
    logic.concatenate = True
    logic.insert(value=".")
    assert logic.concatenate == True


def test_perform_last_input_operator_true(mock):
    operation = "division"
    logic = LogicController(ui=mock)
    logic.last_input_was_operator = True
    logic.operation = "addition"
    logic.perform(operation=operation)
    assert logic.operation == operation
    assert logic.last_input_was_operator
    assert logic.answer == None


def test_perform_operation_true(mock):
    mock.get.return_value = 5
    operation = "division"
    logic = LogicController(ui=mock)
    logic.operation = "addition"
    logic.perform(operation=operation)


def test_perform_except_error(mock):
    mock.get.return_value = "A string"
    operation = "division"
    logic = LogicController(ui=mock)
    logic.operation = None
    logic.answer = 5
    logic.perform(operation=operation)
    assert logic.values == [5]


def test_calculate_operation_true(mock):
    value = 5
    mock.get.return_value = value
    logic = LogicController(ui=mock)
    logic.values = [3]
    logic.operation = "multiplication"
    logic.calculate()
    assert logic.answer == 15
    assert logic.values == []
    assert logic.operation == None
    assert logic.last_input_was_operator == False
    mock.set.assert_called_once_with(text=str(logic.answer))


def test_calculate_operation_false(mock):
    value = 5
    mock.get.return_value = value
    logic = LogicController(ui=mock)
    logic.values = [3]
    logic.operation = None
    logic.calculate()
    assert logic.concatenate == False


def test_calculate_except_zero_division_error(mock):
    mock.get.return_value = 0
    logic = LogicController(ui=mock)
    logic.operation = "division"
    logic.values = [5]
    logic.calculate()
    mock.set.assert_called_once_with(text="Error: Division by Zero")


def test_percentage_no_answer(mock):
    value = ".5"
    mock.get.return_value = value
    logic = LogicController(ui=mock)
    logic.percentage()
    mock.get.assert_called_once()
    mock.set.assert_called_once_with(text=f"{value*100}%")


def test_percentage_except_block():
    logic = LogicController(ui="mock")
    logic.answer = None
    logic.percentage()
    assert logic.answer == None


def test_percentage_with_answer(mock):
    value = 4
    logic = LogicController(ui=mock)
    logic.answer = value
    logic.percentage()
    mock.set.assert_called_once_with(text=f"{value*100}%")


def test_restart(mock):
    mock.get.return_value = 0
    logic = LogicController(ui=mock)
    logic.restart()
    assert logic.values == []
    assert logic.operation == None
    assert logic.concatenate == True
    assert logic.answer == None
    assert logic.last_input_was_operator == False
    mock.set.assert_called_once_with(text="")
    mock.get.return_value = ""
    assert logic.ui.get() == ""
