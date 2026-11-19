# Resistor Color

## 📌 Description
This project is a Python solution to the Exercism **Resistor Color** exercise.

The goal is to convert resistor color bands into their corresponding numerical values. Each color represents a digit from 0 to 9.

The program takes a list of colors and returns a two-digit number based on the first two colors. Any additional colors are ignored.

## 🎨 Color Code Reference

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
2. Use the `index()` method to find the numerical position of the first color.
3. Find the numerical position of the second color.
4. Convert both numbers into strings.
5. Concatenate the strings to create a two-digit number.
6. Convert the final result back into an integer.
7. Ignore all colors after the first two.

## 💻 Example

**Input:**
```python
value(["brown", "green", "violet"])
```

**Output:**
```python
15
```

Explanation:
- Brown = 1
- Green = 5
- Violet is ignored.
- Result = 15

## 🧠 Concepts Practiced

- Python functions
- Lists and indexing
- `list.index()` method
- String concatenation
- Type conversion (`str()` and `int()`)
- Returning values from functions

## 🚀 What I Learned

Through this exercise, I practiced using list indexes to map elements to numerical values. I also learned how to concatenate two numbers using string conversion and convert the result back into an integer.

## 🛠️ Technologies

- Python 3
- Exercism

---

**Author:** Parzival592
