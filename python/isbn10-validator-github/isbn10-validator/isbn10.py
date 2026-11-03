def is_valid(isbn):
    """Return True if isbn is a valid ISBN-10, otherwise False."""

    # Remove optional hyphens.
    isbn = isbn.replace("-", "")

    # An ISBN-10 must contain exactly 10 characters.
    if len(isbn) != 10:
        return False

    # The first nine characters must be digits.
    for char in isbn[:9]:
        if not char.isdigit():
            return False

    # The final character must be a digit or uppercase X.
    if not (isbn[-1].isdigit() or isbn[-1] == "X"):
        return False

    # Calculate the weighted checksum.
    total = 0

    for i in range(10):
        if isbn[i] == "X":
            digit = 10
        else:
            digit = int(isbn[i])

        total += digit * (10 - i)

    # A valid ISBN-10 has a checksum divisible by 11.
    return total % 11 == 0


if __name__ == "__main__":
    examples = [
        ("3-598-21508-8", True),
        ("3598215088", True),
        ("3-598-21507-X", True),
        ("3598215089", False),
        ("359X215078", False),
        ("1234567890", False),
    ]

    for isbn, expected in examples:
        result = is_valid(isbn)
        print(f"{isbn}: {result} (expected: {expected})")
