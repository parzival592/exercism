# Resistor Color

## 📌 Description

This project is part of the Python track on Exercism.

The goal of this exercise is to work with resistor color codes and convert color names into their corresponding numerical values.

Each resistor color represents a number from 0 to 9.

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

## ⚙️ Functions

### 1. `color_code(color)`

Returns the numerical value associated with a given resistor color.

**Examples:**
```python
color_code("black")  # 0
color_code("green")  # 5
color_code("white")  # 9
```

### 2. `colors()`

Returns a list containing all ten resistor colors in the correct order.

**Example:**
```python
colors()
```

Output:
```python
["black", "brown", "red", "orange", "yellow",
 "green", "blue", "violet", "grey", "white"]
```

## 🧠 Concepts Learned

Through this exercise, I practiced:

- Python lists
- List indexing
- The `.index()` method
- Functions and return statements
- Working with ordered data

## 💡 Key Takeaway

Python list indexing starts at `0`. Since resistor colors are arranged in numerical order, the index of each color directly represents its numerical value.

For example:
```python
color_list.index("green")  # 5
```

## 🚀 Technologies

- Python 3
- Exercism Python Track

## 📚 Reference

[Electronic Color Code – Wikipedia](https://en.wikipedia.org/wiki/Electronic_color_code)
