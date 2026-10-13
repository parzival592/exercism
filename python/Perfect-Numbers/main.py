
def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    divisors = []

    for divisor in range(1, number):
        if number % divisor == 0:
            divisors.append(divisor)
            
    result = sum(divisors)
    if result == number:
        return "perfect"
    elif result > number:
        return "abundant"
    else:
        return "deficient"
        