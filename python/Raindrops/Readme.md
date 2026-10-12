# Raindrops — Python (Exercism)

## 1. Problem Overview

The Raindrops exercise is a variation of the classic FizzBuzz programming challenge.

The goal is to write a function named `convert(number)` that converts a number into a string based on its divisibility by 3, 5, and 7.

### Rules

* If the number is divisible by 3, add `"Pling"` to the result.
* If the number is divisible by 5, add `"Plang"` to the result.
* If the number is divisible by 7, add `"Plong"` to the result.
* If the number is not divisible by any of these numbers, return the original number as a string.

If multiple conditions are true, combine the corresponding words in this order:

`Pling` → `Plang` → `Plong`

There should be no spaces between the words.

---

## 2. Examples

| Input | Divisibility                | Expected Output     |
| ----: | --------------------------- | ------------------- |
|    28 | Divisible by 7              | `"Plong"`           |
|    30 | Divisible by 3 and 5        | `"PlingPlang"`      |
|    21 | Divisible by 3 and 7        | `"PlingPlong"`      |
|    35 | Divisible by 5 and 7        | `"PlangPlong"`      |
|   105 | Divisible by 3, 5, and 7    | `"PlingPlangPlong"` |
|    34 | Not divisible by 3, 5, or 7 | `"34"`              |

---

## 3. What I Learned

### 3.1. Functions and Parameters

I learned that a function receives input through its parameters.

For this exercise:

* `def` defines a function.
* `convert` is the function name.
* `number` is the parameter.

The Exercism testing system passes the number directly to the function.

Therefore, I do not need to use `input()` to ask the user for a number.

### 3.2. The Modulo Operator (`%`)

The modulo operator returns the remainder after division.

Examples:

* `12 % 3` returns `0`.
* `14 % 3` returns `2`.
* `15 % 5` returns `0`.

If the remainder is zero, the number is divisible by that divisor.

For example, to determine whether a number is divisible by 3, I check whether the remainder of division by 3 equals zero.

This is the main mathematical concept behind the exercise.

### 3.3. Conditional Statements (`if`)

I learned how to use `if` statements to check conditions.

Each Raindrops rule requires its own independent check because one number can satisfy multiple conditions.

For example, 15 is divisible by both 3 and 5.

The result must therefore contain both `"Pling"` and `"Plang"`.

### 3.4. Why Independent `if` Statements Matter

Initially, I needed to understand why the function should not immediately return a word when it finds a matching condition.

If the function returns `"Pling"` immediately after checking divisibility by 3, it stops running and never checks divisibility by 5 or 7.

This produces incorrect results for numbers that satisfy multiple conditions.

The correct approach is to check all three conditions before returning the final result.
