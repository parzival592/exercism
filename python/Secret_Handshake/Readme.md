# Secret Handshake

## Description

The Secret Handshake exercise converts a binary string into a sequence of secret handshake actions.

Each binary digit represents a specific action. The binary string is processed from right to left to determine which actions should be performed.

If the leftmost (fifth) bit is `1`, the order of all selected actions must be reversed.

## Handshake Actions

| Binary Position | Action |
|---|---|
| `00001` | wink |
| `00010` | double blink |
| `00100` | close your eyes |
| `01000` | jump |
| `10000` | Reverse the order of actions |

## Example

**Input:**

```python
commands("11010")
```

Binary representation:

```text
11010
```

Processing from right to left:

1. `0` → No action.
2. `1` → double blink.
3. `0` → No action.
4. `1` → jump.
5. `1` → Reverse the actions.

**Output:**

```python
["jump", "double blink"]
```

## Python Concepts Learned

- **Functions:** Defining functions and working with parameters.
- **Lists:** Storing multiple actions.
- **For loops:** Iterating through a string.
- **Enumerate():** Accessing both index and value.
- **Reversed():** Processing a string or collection from right to left.
- **If/Elif:** Implementing conditional logic.
- **Append():** Adding elements to a list.
- **List.reverse():** Reversing the order of elements.

## Implementation Approach

1. Receive a binary string as a function argument.
2. Create an empty list to store the actions.
3. Iterate through the binary string from right to left.
4. Use `enumerate()` to identify each digit's position.
5. Check whether the current digit is `1`.
6. Append the corresponding action to the result list.
7. If the fifth bit is `1`, reverse the result list.
8. Return the final list.

## Understanding `reversed()` vs `.reverse()`

Both are used to reverse elements in Python, but they work differently.

### 1. `reversed()` — Built-in Function

`reversed()` returns an iterator that allows you to read elements in reverse order.

It does **not modify the original object**.

Example:

```python
numbers = [1, 2, 3, 4, 5]

for number in reversed(numbers):
    print(number)
```

Output:

```text
5
4
3
2
1
```

The original list remains unchanged:

```python
print(numbers)
```

Output:

```python
[1, 2, 3, 4, 5]
```

**Important points:**
- It is a built-in Python function.
- It returns an iterator.
- It doesn't modify the original list.
- It can be used with strings and lists.

### 2. `.reverse()` — List Method

`.reverse()` is a method that belongs to Python lists.

It modifies the original list directly.

Example:

```python
numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print(numbers)
```

Output:

```python
[5, 4, 3, 2, 1]
```

**Important points:**
- It is a list method.
- It modifies the original list.
- It returns `None`.



