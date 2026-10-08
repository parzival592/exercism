def equilateral(sides):
    a, b, c = sides

    if a <= 0 or b <= 0 or c <= 0:
        return False

    if a + b < c or a + c < b or b + c < a:
        return False

    return a == b == c


def isosceles(sides):
    a, b, c = sides

    if a <= 0 or b <= 0 or c <= 0:
        return False

    if a + b < c or a + c < b or b + c < a:
        return False

    return a == b or b == c or a == c


def scalene(sides):
    a, b, c = sides

    if a <= 0 or b <= 0 or c <= 0:
        return False

    if a + b < c or a + c < b or b + c < a:
        return False

    return a != b and b != c and a != c