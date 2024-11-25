from operator import add, sub, mul, truediv

operations = {
    "addition": {"calculation": add, "symbol": "+", "row": 4},
    "subtraction": {"calculation": sub, "symbol": "-", "row": 3},
    "multiplication": {"calculation": mul, "symbol": "*", "row": 2},
    "division": {"calculation": truediv, "symbol": "÷", "row": 1},
}
