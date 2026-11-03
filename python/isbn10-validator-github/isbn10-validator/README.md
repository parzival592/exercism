# ISBN-10 Validator

A beginner-friendly Python implementation that validates ISBN-10 book identifiers.

## Features

- Accepts ISBN-10 values with or without hyphens.
- Checks that the ISBN contains exactly 10 characters after removing hyphens.
- Validates the first nine characters as digits.
- Accepts a digit (`0–9`) or uppercase `X` as the check character.
- Calculates the ISBN-10 checksum using weights from 10 down to 1.
- Returns `True` for a valid ISBN-10 and `False` otherwise.

## How ISBN-10 validation works

An ISBN-10 contains 10 characters:

- The first nine characters must be digits.
- The final character must be a digit or `X`.
- `X` represents the value `10`.
- Hyphens are optional and are ignored during validation.

The checksum is calculated as:

```text
(d1 × 10 + d2 × 9 + d3 × 8 + ... + d9 × 2 + d10 × 1) mod 11
```

The ISBN is valid when the remainder is `0`.

## Project structure

```text
isbn10-validator/
├── isbn10.py
├── test_isbn10.py
└── README.md
```

## Requirements

- Python 3.8 or newer
- No external packages required

## Run the program

Run the example tests:

```bash
python isbn10.py
```

Run the unit tests:

```bash
python -m unittest -v
```

## Example

```python
from isbn10 import is_valid

print(is_valid("3-598-21508-8"))  # True
print(is_valid("3598215088"))     # True
print(is_valid("3-598-21507-X"))  # True
print(is_valid("3598215089"))     # False
print(is_valid("359X215078"))     # False
```

## Concepts practiced

- Functions and parameters
- String methods: `replace()` and `isdigit()`
- String slicing: `isbn[:9]`
- Negative indexing: `isbn[-1]`
- `for` loops and `range()`
- Type conversion with `int()`
- Conditional statements
- Boolean operators: `not` and `or`
- Accumulator variables with `+=`
- Modulo operator: `%`
- Unit testing with `unittest`

## Notes

This project validates the ISBN-10 format and checksum. It does not verify that an ISBN has actually been assigned to a published book.

## License

This project is available under the MIT License. Add a `LICENSE` file if you want to distribute it under that license.
