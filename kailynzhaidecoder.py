def decode(to_decode):
    s = ""
    for digit in str(to_decode):
        if int(digit) > 2:
            s = s + str(int(digit) - 3)
        elif int(digit) == 2:
            s = s + "9"
        elif int(digit) == 1:
            s = s + "8"
        else:
            s = s + "7"
    return s
