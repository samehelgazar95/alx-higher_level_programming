#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argsLen = len(sys.argv) - 1
    if argsLen == 0:
        print("0 arguments.")
    elif argsLen == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argsLen))
    for i in range(argsLen):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
