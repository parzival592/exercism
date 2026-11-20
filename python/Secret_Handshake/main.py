def command(binary_str):
    result =  []

    for index, digit in enumerate(reversed(binary_str)):

        if digit == "1":
                if index == 0:
                    result.append("wink")
                if index == 1:
                    result.append("double blink")
                if index == 2:
                    result.append("close your eyes")
                if index == 3:
                    result.append("jump")
        
                if index == 4:
                    result.reverse()
    return result 
        


    