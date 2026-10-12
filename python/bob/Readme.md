# Bob — Python Exercise

## 1. Introduction

Bob is a teenager who doesn't like showing much emotion. When someone talks to him, he responds with one of five possible answers depending on what the person says.

The goal of this exercise is to write a Python function that analyzes a message and returns Bob's appropriate response.

### Bob's responses

| Situation                                        | Response                            |
| ------------------------------------------------ | ----------------------------------- |
| The message is empty or contains only whitespace | `Fine. Be that way!`                |
| Someone yells a question at Bob                  | `Calm down, I know what I'm doing!` |
| Someone yells at Bob                             | `Whoa, chill out!`                  |
| Someone asks a normal question                   | `Sure.`                             |
| Anything else                                    | `Whatever.`                         |

---

## 2. Python Concepts Learned

### 2.1 Functions

A function is a reusable block of code that performs a particular task.

In this exercise, the function is named `response`.

It receives a message as input, analyzes it, and returns Bob's response.

**Important concepts:**

* `def` defines a function.
* `response` is the function's name.
* `hey_bob` is a parameter that receives the message.
* `return` sends the result back to the caller.

Example:

```python
def response(hey_bob):
    return "Whatever."
```

Calling the function with a message returns the specified response.

The example above demonstrates the basic function structure, not the complete exercise solution.

### 2.2 Conditional Statements

Conditional statements allow a program to make decisions.

Python provides three commonly used conditional keywords:

* `if` — executes a block when a condition is true.
* `elif` — checks another condition if the preceding conditions were false.
* `else` — handles cases where none of the preceding conditions matched.

In this exercise, conditional statements determine which response Bob should return.

For example, the program first checks whether the message is empty before examining other possibilities.

### 2.3 Boolean Values

Boolean values represent whether something is true or false.

Python has two Boolean values:

* `True`
* `False`

For example, checking whether a message ends with a question mark produces a Boolean result.

If the message is `"How are you?"`, the result is `True`.

If the message is `"Hello!"`, the result is `False`.

These results allow conditional statements to make decisions.

### 2.4 The `not` Operator

The `not` operator reverses a Boolean value.

| Expression  | Result  |
| ----------- | ------- |
| `not True`  | `False` |
| `not False` | `True`  |

In this exercise, `not` is used to detect an empty message after removing whitespace.

An empty string is considered false in a Boolean context. Applying `not` makes that condition true.

### 2.5 The `and` Operator

The `and` operator combines conditions.

Both conditions must be true for the complete expression to be true.

| First condition | Second condition | Result  |
| --------------- | ---------------- | ------- |
| `True`          | `True`           | `True`  |
| `True`          | `False`          | `False` |
| `False`         | `True`           | `False` |
| `False`         | `False`          | `False` |

For Bob's exercise, a yelled question must satisfy two conditions:

1. The message must be uppercase.
2. The message must end with a question mark.

If either condition is false, the message does not qualify as a yelled question.

---

## 3. String Methods

Python strings have built-in methods that help us inspect and manipulate text.

### 3.1 `.strip()`

The `.strip()` method removes whitespace from the beginning and end of a string.

Examples:

| Original string | Result    |
| --------------- | --------- |
| `"Hello"`       | `"Hello"` |
| `"   "`         | `""`      |
| `"  Hello  "`   | `"Hello"` |
| `"\n\t"`        | `""`      |

Whitespace includes spaces, tabs, and newline characters.

In this exercise, `.strip()` helps identify messages that contain only whitespace.

For example, a message containing three spaces is not technically an empty string. However, after stripping the spaces, it becomes empty.

**Important:** `.strip()` removes whitespace only from the beginning and end, not from the middle of a string.

### 3.2 `.isupper()`

The `.isupper()` method checks whether a string's cased characters are uppercase.

Examples:

| String     | Result  |
| ---------- | ------- |
| `"HELLO"`  | `True`  |
| `"HELLO!"` | `True`  |
| `"Hello"`  | `False` |
| `"hello"`  | `False` |
| `"12345"`  | `False` |

Numbers, spaces, and punctuation do not have uppercase or lowercase forms.

A string containing no cased characters returns `False` when checked with `.isupper()`.

This method helps identify messages that represent yelling.

However, it should not be the only check used to identify yelling, because the message must also contain at least one letter.

### 3.3 `.endswith()`

The `.endswith()` method checks whether a string ends with a particular sequence of characters.

Examples:

| String            | Expression                      | Result  |
| ----------------- | ------------------------------- | ------- |
| `"Hello?"`        | `"Hello?".endswith("?")`        | `True`  |
| `"Hello!"`        | `"Hello!".endswith("?")`        | `False` |
| `"Are you okay?"` | `"Are you okay?".endswith("?")` | `True`  |

The method needs an argument specifying what the string should end with.

In this exercise, the question mark is used to identify questions.

### 3.4 `.isalpha()`

The `.isalpha()` method checks whether every character in a nonempty string is alphabetic.

Examples:

| String          | Result  |
| --------------- | ------- |
| `"HELLO"`       | `True`  |
| `"Hello"`       | `True`  |
| `"STOP!"`       | `False` |
| `"HELLO WORLD"` | `False` |
| `"12345"`       | `False` |

The important distinction is that `.isalpha()` checks whether **all characters are letters**, not whether a string contains at least one letter.

This matters because `"STOP!"` is clearly a yelled message, even though `.isalpha()` returns `False` for it.

To solve this problem, we need another technique.

---

## 4. The `any()` Function

The built-in `any()` function checks whether at least one item in an iterable satisfies a condition.

It returns:

* `True` if at least one item is true.
* `False` if every item is false or the iterable is empty.

For example, imagine the following Boolean values:

```text
True, False, False
```

Because at least one value is `True`, `any()` returns `True`.

Now consider:

```text
False, False, False
```

Because every value is `False`, `any()` returns `False`.

### 4.1 Checking Whether a Message Contains a Letter

The expression used in this exercise is:

```python
any(char.isalpha() for char in hey_bob)
```

This expression combines three concepts.

**First: `for char in hey_bob`**

This examines each character in the message, one at a time.

If the message is `"STOP!"`, the characters are:

```text
S
T
O
P
!
```

The variable `char` represents the current character being examined.

**Second: `char.isalpha()`**

This checks whether the current character is a letter.

For `"STOP!"`, the results are:

| Character | Result of `.isalpha()` |
| --------- | ---------------------- |
| `S`       | `True`                 |
| `T`       | `True`                 |
| `O`       | `True`                 |
| `P`       | `True`                 |
| `!`       | `False`                |

**Third: `any()`**

The `any()` function combines these results.

Because at least one character is a letter, the expression returns `True`.

Consider another message:

```text
12345!
```

None of its characters are letters, so the expression returns `False`.

### 4.2 Why This Is Useful

The goal is to recognize yelling without mistakenly treating numbers or punctuation as yelling.

| Message         | Contains a letter? | Result  |
| --------------- | ------------------ | ------- |
| `"STOP!"`       | Yes                | `True`  |
| `"I AM ANGRY!"` | Yes                | `True`  |
| `"12345"`       | No                 | `False` |
| `"!!!"`         | No                 | `False` |

Combining `any()` with `.isalpha()` makes it possible to check whether a message contains at least one letter, even when the message also contains spaces, numbers, or punctuation.

This is a useful example of how Python's built-in functions can simplify string-processing tasks.

---

## 5. Complete Solution

The following is the complete solution for the exercise.

```python
def response(hey_bob):
    if not hey_bob.strip():
        return "Fine. Be that way!"

    if hey_bob.isupper() and hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!"

    if hey_bob.isupper() and any(char.isalpha() for char in hey_bob):
        return "Whoa, chill out!"

    if hey_bob.endswith("?"):
        return "Sure."

    else:
        return "Whatever."
```

---

## 6. Explanation of the Solution

### Condition 1: Silence

```python
if not hey_bob.strip():
    return "Fine. Be that way!"
```

The program removes whitespace from both ends of the message.

If nothing remains, the message is empty or contains only whitespace.

Bob returns:

`Fine. Be that way!`

### Condition 2: Yelling a Question

```python
if hey_bob.isupper() and hey_bob.endswith("?"):
    return "Calm down, I know what I'm doing!"
```

The program checks two conditions:

1. The message's cased letters are uppercase.
2. The message ends with a question mark.

Both must be true.

Example:

Input: `"ARE YOU OK?"`

Output: `"Calm down, I know what I'm doing!"`

### Condition 3: Yelling

```python
if hey_bob.isupper() and any(char.isalpha() for char in hey_bob):
    return "Whoa, chill out!"
```

The program checks whether the message is uppercase and contains at least one letter.

Example:

Input: `"STOP!"`

Output: `"Whoa, chill out!"`

The `any()` function prevents messages containing only numbers or punctuation from being treated as yelling.

### Condition 4: A Normal Question

```python
if hey_bob.endswith("?"):
    return "Sure."
```

If the message ends with a question mark and has not already matched an earlier condition, Bob returns:

`Sure.`

Example:

Input: `"How are you?"`

Output: `"Sure."`

### Condition 5: Anything Else

```python
else:
    return "Whatever."
```

If the preceding conditions do not return a response, Bob returns the default answer.

Example:

Input: `"Hello there."`

Output: `"Whatever."`

---

## 7. Why the Order of Conditions Matters

The order is important because a message can satisfy multiple conditions.

Consider:

`"ARE YOU OK?"`

This message is both uppercase and a question.

If the program checked ordinary yelling before checking yelled questions, it could return the wrong response.

Therefore, the program checks yelled questions first.

The decision order is:

1. Silence.
2. Yelling a question.
3. Ordinary yelling.
4. A normal question.
5. Anything else.

This demonstrates an important programming principle: **when conditions overlap, evaluate the more specific conditions before the more general ones.**

---

## 8. Test Cases

The following test cases cover the five possible responses and several edge cases.

| Input            | Expected output                       | Reason                                        |
| ---------------- | ------------------------------------- | --------------------------------------------- |
| `""`             | `"Fine. Be that way!"`                | Empty message                                 |
| `"   "`          | `"Fine. Be that way!"`                | Whitespace only                               |
| `"\n\t"`         | `"Fine. Be that way!"`                | Whitespace characters                         |
| `"ARE YOU OK?"`  | `"Calm down, I know what I'm doing!"` | Yelled question                               |
| `"HELLO?"`       | `"Calm down, I know what I'm doing!"` | Uppercase question                            |
| `"STOP"`         | `"Whoa, chill out!"`                  | Uppercase letters                             |
| `"STOP!"`        | `"Whoa, chill out!"`                  | Uppercase letters with punctuation            |
| `"I AM ANGRY!"`  | `"Whoa, chill out!"`                  | Uppercase letters with spaces and punctuation |
| `"How are you?"` | `"Sure."`                             | Normal question                               |
| `"Hello there."` | `"Whatever."`                         | Ordinary statement                            |
| `"12345"`        | `"Whatever."`                         | Numbers only                                  |
| `"!!!"`          | `"Whatever."`                         | Punctuation only                              |

---

## 9. What I Learned

By completing this exercise, I practiced:

* Defining functions and using parameters.
* Returning values with `return`.
* Using `if` and `else` to control program flow.
* Combining Boolean conditions with `and`.
* Reversing conditions with `not`.
* Removing whitespace with `.strip()`.
* Checking uppercase text with `.isupper()`.
* Checking string endings with `.endswith()`.
* Checking alphabetic characters with `.isalpha()`.
* Iterating through strings with `for`.
* Using `any()` to check whether at least one condition is true.
* Handling overlapping conditions in the correct order.
* Testing a function with normal inputs and edge cases.

### Main Takeaway

This exercise taught me how to break a problem into smaller conditions and combine Python's built-in string methods with Boolean logic.

Instead of treating every message the same way, the function examines its characteristics and selects the appropriate response.

The same approach can be useful in input validation, text processing, form handling, and other programming tasks.
