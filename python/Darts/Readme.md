# Darts — Exercism Python

## 📌 About the Exercise

The goal of this exercise is to calculate the score of a dart based on where it lands on a circular target.

The target has three concentric circles centered at the coordinates `(0, 0)`.

The score depends on the distance between the dart's landing position and the center of the target.

## 🎯 Scoring Rules

| Distance from the Center |     Score |
| ------------------------ | --------: |
| `distance <= 1`          | 10 points |
| `distance <= 5`          |  5 points |
| `distance <= 10`         |   1 point |
| `distance > 10`          |  0 points |

**Important:** The boundary of each circle is included in its scoring region.

For example, a dart exactly 5 units from the center earns 5 points.

## 🧮 Mathematical Concept

To determine where the dart lands, we calculate its distance from the center using the Euclidean distance formula:

$$
d = \sqrt{x^2+y^2}
$$

Where:

* `x` is the horizontal coordinate.
* `y` is the vertical coordinate.
* `d` is the distance from the center `(0, 0)`.

In Python, the formula is:

```python
distance = (x ** 2 + y ** 2) ** 0.5
```

### Example

Suppose the dart lands at `(3, 4)`.

$$
d = \sqrt{3^2+4^2}
$$

$$
d = \sqrt{9+16} = \sqrt{25} = 5
$$

Since the distance is 5, the dart earns 5 points.

## 💻 Python Solution

```python
def score(x, y):
    distance = (x ** 2 + y ** 2) ** 0.5

    if distance <= 1:
        return 10
    elif distance <= 5:
        return 5
    elif distance <= 10:
        return 1
    else:
        return 0
```
