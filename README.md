# Calculadora
This is a simple calculator app built using Python's customtkinter library. It allows users to perform basic arithmetic operations like addition, subtraction, multiplication, and division. The app features a clean and responsive user interface with buttons for numbers, operators, and a result display.

## Features
- Perform basic arithmetic operations: `+`, `-`, `*`, `/`
- Support for decimal numbers
- Handle zero division errors
- Clear and equals buttons for restarting and calculating results

## How It Works
### Structure
- `main.py`: Entry point of the application, where the app window and buttons are created. This file connects all components together.
- `app.py`: Contains the `App` class that initializes the application window.
- `button.py`: Contains the `GuiButton` class, which is used to create and configure the calculator buttons.
- `label.py`: Contains the `GuiLabel` class, responsible for the display label (where the result is shown).
- `logic.py`: Contains the `LogicController` class that handles all the business logic behind the calculator, such as operations and calculations.
- `ui.py`: Contains the `UiController` class that acts as an intermediary between the logic and the user interface, updating the display when necessary.
- `operations.py`: Contains the definitions of the calculator operations (addition, subtraction, multiplication, division).

### Main Components
- `UiController`:
  Handles the updates and retrievals of the calculator display (label).
  Decouples the UI updates from the `LogicController` class.
- `LogicController`:
  Manages the calculator’s internal state (like the current input, stored values, and selected operation).
  Computes the results and passes them to the `UiController` for display.
- `GuiButton`:
  Manages button creation and configuration.
  Each button is linked to the appropriate method in the `LogicController`.
- `GuiLabel`:
  Responsible for rendering the display (e.g., current input, calculation results).
