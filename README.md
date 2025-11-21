# testRepository

A simple Python mathematics utility library providing basic arithmetic operations.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Examples](#examples)
- [Code Organization](#code-organization)
- [Key Components](#key-components)
  - [Math Module](#math-module)
- [Development](#development)
  - [Running Tests](#running-tests)
  - [Code Style](#code-style)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview

`testRepository` is a lightweight Python library that provides fundamental mathematical operations. This project demonstrates clean code practices with type hints and a modular structure. It serves as a foundation for building more complex mathematical utilities or as a reference for Python project organization.

**Owner:** nborges-aws

## Features

- ✅ Basic arithmetic operations (addition)
- ✅ Type hints for better code clarity and IDE support
- ✅ Simple and intuitive API
- ✅ Lightweight with no external dependencies
- ✅ Python 3.x compatible

## Repository Structure

```
testRepository/
│
├── src/
│   └── Math.py          # Core mathematics module with arithmetic operations
│
└── README.md            # Project documentation (this file)
```

### Directory Breakdown

- **`src/`**: Contains all source code files
  - **`Math.py`**: The main module implementing mathematical operations

## Setup Instructions

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.6 or higher**: This project uses type hints which require Python 3.5+
- **pip**: Python package installer (usually comes with Python)

You can verify your Python installation by running:

```bash
python --version
# or
python3 --version
```

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/nborges-aws/testRepository.git
   cd testRepository
   ```

2. **Set up your Python environment** (optional but recommended):

   ```bash
   # Create a virtual environment
   python -m venv venv
   
   # Activate the virtual environment
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Add the project to your Python path** (if needed):

   You can either:
   - Add the repository root to your `PYTHONPATH` environment variable
   - Install in development mode (once setup.py is added)
   - Import modules using relative paths

## Usage

### Basic Usage

To use the mathematics utilities in your Python code, import the necessary functions from the `src.Math` module:

```python
from src.Math import add

# Perform addition
result = add(5, 3)
print(f"5 + 3 = {result}")  # Output: 5 + 3 = 8
```

### Examples

#### Example 1: Simple Addition

```python
from src.Math import add

# Adding two positive integers
result = add(10, 20)
print(result)  # Output: 30
```

#### Example 2: Working with Negative Numbers

```python
from src.Math import add

# Adding positive and negative integers
result = add(15, -5)
print(result)  # Output: 10

# Adding two negative integers
result = add(-10, -20)
print(result)  # Output: -30
```

#### Example 3: Using in a Script

Create a file named `example.py`:

```python
#!/usr/bin/env python3
from src.Math import add

def calculate_total(prices):
    """Calculate the total of a list of prices."""
    total = 0
    for price in prices:
        total = add(total, price)
    return total

if __name__ == "__main__":
    prices = [10, 25, 30, 15]
    total = calculate_total(prices)
    print(f"Total: ${total}")  # Output: Total: $80
```

Run it with:
```bash
python example.py
```

## Code Organization

The project follows a simple, modular structure:

### Module Design

- **Separation of Concerns**: Mathematical operations are isolated in dedicated modules
- **Type Safety**: All functions use type hints for parameters and return values
- **Documentation**: Code is written to be self-documenting with clear function names

### Naming Conventions

- **Functions**: Use lowercase with underscores (snake_case)
- **Variables**: Use lowercase with underscores (snake_case)
- **Type Hints**: Use Python's built-in type hint system for clarity

## Key Components

### Math Module

**Location:** `src/Math.py`

This module contains the core mathematical operations provided by the library.

#### Functions

##### `add(a: int, b: int) -> int`

Adds two integers and returns their sum.

**Parameters:**
- `a` (int): The first integer operand
- `b` (int): The second integer operand

**Returns:**
- `int`: The sum of `a` and `b`

**Example:**
```python
result = add(7, 3)  # Returns 10
```

**Implementation Details:**
- Uses Python's built-in addition operator (`+`)
- Handles both positive and negative integers
- Returns an integer result
- Type-safe with explicit type hints

## Development

### Running Tests

Currently, the project does not include a test suite. To add tests, consider using:

**pytest:**
```bash
# Install pytest
pip install pytest

# Create a tests directory
mkdir tests
```

Example test file (`tests/test_math.py`):
```python
from src.Math import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_mixed_numbers():
    assert add(10, -5) == 5
```

Run tests with:
```bash
pytest tests/
```

### Code Style

This project follows Python best practices:

- **PEP 8**: Python's style guide for code formatting
- **Type Hints**: Using Python 3.5+ type hint syntax
- **Docstrings**: Recommended for all public functions (to be added)

To check code style:
```bash
# Install flake8
pip install flake8

# Run style checker
flake8 src/
```

To format code automatically:
```bash
# Install black
pip install black

# Format code
black src/
```

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Add tests** for your changes
5. **Commit your changes:**
   ```bash
   git commit -m "Add your descriptive commit message"
   ```
6. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Open a Pull Request**

### Ideas for Contribution

- Add more mathematical operations (subtract, multiply, divide)
- Implement support for floating-point numbers
- Add comprehensive test coverage
- Create documentation with examples
- Add error handling for edge cases
- Implement more advanced mathematical functions (power, modulo, etc.)
- Add CI/CD pipeline configuration

## License

Please add an appropriate license file to specify the terms under which this software can be used.

Common options include:
- MIT License (permissive)
- Apache License 2.0 (permissive with patent grant)
- GPL (copyleft)

## Contact

**Repository Owner:** nborges-aws

For questions, issues, or suggestions, please:
- Open an issue in the GitHub repository
- Contact the repository owner

---

**Note:** This is a basic implementation intended for educational purposes or as a starting point for more complex mathematical utilities. For production use, consider using established libraries like NumPy for mathematical operations.
