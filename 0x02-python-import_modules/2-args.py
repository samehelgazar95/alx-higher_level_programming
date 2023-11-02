#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argsLen = len(sys.argv)

    if argsLen == 1:
        print("0 arguments.")
    elif argsLen == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(argsLen-1))

    for i in range(argsLen-1):
        print("{}: {}".format(i+1, sys.argv[i+1]))
