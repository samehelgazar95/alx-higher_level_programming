#!/usr/bin/python3
import sys
args = sys.argv
argsLen = len(args)

if argsLen == 1:
    print("0 arguments.")
elif argsLen == 2:
    print('''1 argument:
1: {}'''.format(args[1]))
else:
    print("{} arguments:". format(argsLen))
    for i in range(1, argsLen):
        print("{}: {}".format(i, args[i]))
