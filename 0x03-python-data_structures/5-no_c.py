def no_c(my_string):
    output = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            i = ""
        output += i
