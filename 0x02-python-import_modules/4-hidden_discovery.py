#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    cp = dir(hidden_4)
    for i in cp:
        if i[0:2] != "__":
            print("{}".format(i))
