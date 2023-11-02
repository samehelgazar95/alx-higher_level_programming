#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    argsLen = len(args)

    if argsLen == 1:
        print("0 arguments.")
    elif argsLen == 2:
        print("1 argument:")
        print("1: {}".format(args[1]))
    else:
        print("{} arguments:". format(argsLen-1))
        for i in range(1, argsLen):
            print("{}: {}".format(i, args[i]))
