def resistor_label(colors):
    colours = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

    tolerance_colours = {
        "brown": "±1%",
        "red": "±2%",
        "green": "±0.5%",
        "blue": "±0.25%",
        "violet": "±0.1%",
        "grey": "±0.05%",
        "gold": "±5%",
        "silver": "±10%"
    }

    if len(colors) == 1:
        return f"{colours.index(colors[0])}Ω"
    elif len(colors) == 4:
        first_index = colours.index(colors[0])
        second_index = colours.index(colors[1])
        third_index = colours.index(colors[2])
        tolerance_value = tolerance_colours[colors[3]]

        main_number = first_index * 10 + second_index
        result = main_number * (10 ** third_index)
        if result < 1000:
            return f"{result}Ω {tolerance_value}"
        elif result < 1000000:
            return f"{result / 1000}kΩ {tolerance_value}"   
        elif result < 1000000000:
            return f"{result / 1000000}MΩ {tolerance_value}"
        else:
            return f"{result / 1000000000}GΩ {tolerance_value}" 
    elif len(colors) == 5:
        first_index = colours.index(colors[0])
        second_index = colours.index(colors[1])
        third_index = colours.index(colors[2])
        fourth_index = colours.index(colors[3])
        tolerance_value = tolerance_colours[colors[4]]

        main_number = first_index * 100 + second_index * 10 + third_index
        result = main_number * (10 ** fourth_index)
        if result < 1000:
            return f"{result}Ω {tolerance_value}"
        elif result < 1000000:
            return f"{result / 1000}kΩ {tolerance_value}"   
        elif result < 1000000000:
            return f"{result / 1000000}MΩ {tolerance_value}"
        else:
            return f"{result / 1000000000}GΩ {tolerance_value}"
        