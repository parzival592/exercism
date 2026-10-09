
def is_armstrong_number(number):
    digits = str(number)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return total == number
