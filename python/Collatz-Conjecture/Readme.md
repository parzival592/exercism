# Collatz Conjecture — Python

## Overview

The Collatz Conjecture is a mathematical problem that starts with a positive integer and repeatedly applies two rules until the number reaches `1`.

The goal of this exercise is to calculate how many steps are required to reach `1`.

## Rules

Given a positive integer:

1. If the number is even, divide it by `2`.
2. If the number is odd, multiply it by `3` and add `1`.
3. Repeat these operations until the number becomes `1`.
4. Return the total number of steps.

If the input is zero or negative, the function must raise a `ValueError`.

## Example

Starting number: `12`

The sequence is:

```text
12 → 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
```

The number reaches `1` after **9 steps**.

Therefore:

```python
steps(12)  # Returns 9
```

## Concepts I Learned

### 1. Functions

In Python, a function is a reusable block of code that performs a specific task.

```python
def steps(number):
```

* `def` defines a function.
* `steps` is the function name.
* `number` is the parameter that receives the input.

For example, calling `steps(12)` passes `12` to the function.

### 2. Conditional Statements

Conditional statements allow a program to make decisions.

In this exercise, `if` and `else` determine which mathematical operation to perform.

* Even number: divide by `2`.
* Odd number: multiply by `3` and add `1`.

### 3. The Modulo Operator (`%`)

The modulo operator returns the remainder after division.

Examples:

```python
8 % 2  # 0
7 % 2  # 1
```

If the remainder after dividing by `2` is `0`, the number is even.

Otherwise, for an integer, the number is odd.

This allows the program to choose the correct Collatz rule.

### 4. Integer Division (`//`)

The `//` operator performs floor division.

For positive integers:

```python
8 // 2  # 4
9 // 2  # 4
```

In the Collatz algorithm, we divide an even number by `2`, so the result remains an integer.

### 5. While Loops

A `while` loop repeats a block of code while its condition is true.

```python
while number != 1:
```

This means the loop continues as long as the current number is not `1`.

When the number becomes `1`, the condition becomes false and the loop stops.

### 6. Counting Steps

We initialize a counter:

```python
count = 0
```

The counter starts at zero because no operations have been performed yet.

After each operation, we increment the counter:

```python
count += 1
```

This is shorthand for:

```python
count = count + 1
```

Each time the algorithm changes the number, the counter increases by one.

### 7. Raising Exceptions

The exercise requires invalid inputs to raise a `ValueError`.

```python
if number <= 0:
    raise ValueError("Only positive integers are allowed")
```

* `number <= 0` checks whether the input is invalid.
* `raise` raises an exception.
* `ValueError` identifies the type of error.
* The string provides a meaningful error message.

Validation happens before the loop so that zero and negative inputs are rejected immediately.

### 8. Returning a Value

The `return` statement sends the final result back to the caller.

```python
return count
```

It must be placed outside the loop so that the function finishes the entire calculation before returning the result.

Returning inside the loop would stop the function too early.

## Final Solution

```python
def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    count = 0

    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = (number * 3) + 1

        count += 1

    return count
```

## Test Cases

```python
print(steps(1))   # 0
print(steps(2))   # 1
print(steps(3))   # 7
print(steps(12))  # 9
```

Invalid input examples:

```python
steps(0)   # Raises ValueError
steps(-5)  # Raises ValueError
```

## Mistakes I Corrected

### Mistake 1: Using `input()`

Initially, I considered using `input()` to receive the number.

However, Exercism passes the argument directly to the function. I do not need to ask the user for input.

Also, `input()` returns a string, whereas this exercise expects the function to receive an integer.

### Mistake 2: Returning a Message Instead of Calculating

Initially, I considered returning a message when the number was even.

However, the function must calculate the next number and continue the process until it reaches `1`.

### Mistake 3: Forgetting to Increment the Counter

The counter must increase after every operation.

Without `count += 1`, the function cannot calculate the correct number of steps.

### Mistake 4: Incorrect Counter Assignment

I initially considered writing:

```python
total =+ count
```

This does not increment the counter. It assigns the positive value of `count` to `total`.

The correct increment operation is:

```python
count += 1
```

### Mistake 5: Returning Inside the Loop

Returning inside the loop would terminate the function before the entire sequence was calculated.

The correct approach is to finish the loop and then return the counter.

### Mistake 6: Using Curly Braces

I initially wrote:

```python
return {count}
```

Curly braces create a set containing the counter, not an integer.

The correct statement is:

```python
return count
```

## Algorithm Summary

The solution follows this sequence:

1. Validate the input.
2. Initialize the counter to zero.
3. Repeat while the number is not `1`.
4. Check whether the number is even or odd.
5. Apply the appropriate mathematical operation.
6. Increment the counter.
7. Return the final counter.

## What I Practiced

By completing this exercise, I practiced:

* Defining Python functions and using parameters.
* Writing conditional statements with `if` and `else`.
* Using the modulo operator to check whether a number is even or odd.
* Performing integer division and arithmetic operations.
* Using `while` loops.
* Updating variables during a loop.
* Counting repeated operations.
* Raising exceptions for invalid inputs.
* Returning the correct data type.
* Debugging logical mistakes step by step.

## Conclusion

This exercise helped me understand how to combine conditions, loops, counters, exception handling, and return values to solve a mathematical problem.

The most important lesson was that a working algorithm requires more than correct mathematical operations: the program must also update its state, count each operation, stop at the correct time, and return the expected result.
