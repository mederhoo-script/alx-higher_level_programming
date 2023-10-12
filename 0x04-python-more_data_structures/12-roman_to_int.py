#!/usr/bin/python3
def roman_to_int(roman_string):
    try:
        r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        preva = 0

        for c in roman_string:
            current_value = r[c]
            if current_value > preva:
                result += current_value - 2 * preva
            else:
                result += current_value
            preva = current_value

        return result
    except (TypeError, KeyError):
        return 0
