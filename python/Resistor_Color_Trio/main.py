def label(colors):
    colours = ["black",  "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

    first_index = colours.index(colors[0])
    second_index = colours.index(colors[1])
    third_index = colours.index(colors[2])

    main_number = first_index * 10 + second_index 

    result = main_number * (10 ** third_index)

    if result < 1000:
        return f"{result} ohms"
    if result < 1000000:
        return f"{result / 1000} kiloohms"
    if result < 1000000000:
        return f"{result / 1000000} megaohms"
    else:
        return f"{result / 1000000000} gigaohms"    

    