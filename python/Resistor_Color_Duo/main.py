def values(colors):
    colours = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

    first_index = colours.index(colors[0])
    second_index = colours.index(colors[1])

    result = str(first_index) + str(second_index)
    return int(result)

