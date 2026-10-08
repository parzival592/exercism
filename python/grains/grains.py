def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    number_of_grains_on_the_square = 2 ** (number - 1)
    return number_of_grains_on_the_square


def total():
    return 2 ** 64 - 1