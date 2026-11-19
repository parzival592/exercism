# Resistor Color Trio

## 📌 Description

The Resistor Color Trio exercise is about calculating the resistance value of a resistor using its three color bands.

Each color represents a number from 0 to 9.

- The first color represents the first digit.
- The second color represents the second digit.
- The third color represents the number of zeros to add.

The final resistance value is expressed using metric units.

## 🎨 Color Codes

| Color | Value |
|---|---:|
| Black | 0 |
| Brown | 1 |
| Red | 2 |
| Orange | 3 |
| Yellow | 4 |
| Green | 5 |
| Blue | 6 |
| Violet | 7 |
| Grey | 8 |
| White | 9 |

## ⚙️ How It Works

1. Create a list containing all resistor colors in the correct order.
2. Find the index of each color using `.index()`.
3. Calculate the first two digits.
4. Multiply the number by `10` raised to the power of the third color's index.
5. Convert the result into the appropriate metric unit.

## 📏 Metric Units

| Resistance | Unit |
|---|---|
| Less than 1,000 | Ohms |
| 1,000 – 999,999 | Kiloohms |
| 1,000,000 – 999,999,999 | Megaohms |
| 1,000,000,000 and above | Gigaohms |

## 💻 Example

**Input:**
```python
["orange", "orange", "black"]
```

**Calculation:**

- Orange = 3
- Orange = 3
- Black = 0
- Main number = 33
- Resistance = 33 × 10⁰ = 33

**Output:**
```text
33 ohms
```

## 🧠 What I Learned

- Working with Python lists.
- Finding elements using `.index()`.
- Accessing list elements using indexing.
- Using exponentiation (`**`).
- Performing mathematical calculations.
- Using `if`, `elif`, and `else` conditions.
- Formatting strings using f-strings.
- Converting large numbers into metric units.

## 🛠️ Language

- Python 3

## 📚 Platform

[Exercism – Python Track](https://exercism.org/tracks/python)
