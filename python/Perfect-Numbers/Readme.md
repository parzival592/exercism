# Perfect Numbers — Python

## 📌 Overview

This project solves the **Perfect Numbers** exercise from [Exercism Python Track](https://exercism.org/tracks/python/exercises/perfect-numbers).

The goal is to classify a positive integer into one of three categories:

* **Perfect** — the sum of its proper divisors equals the number.
* **Abundant** — the sum of its proper divisors is greater than the number.
* **Deficient** — the sum of its proper divisors is less than the number.

The classification system is attributed to the ancient Greek mathematician Nicomachus.

## 🧠 What Is a Proper Divisor?

A proper divisor is a positive integer that divides a number evenly, excluding the number itself.

For example, the proper divisors of `6` are:

```text
1, 2, 3
```

Their sum is:

```text
1 + 2 + 3 = 6
```

Therefore, `6` is a perfect number.

## 📚 Number Classifications

### 1. Perfect Number

A number is perfect when the sum of its proper divisors equals the original number.

**Example: 6**

```text
Proper divisors: 1, 2, 3
Sum: 1 + 2 + 3 = 6
Classification: perfect
