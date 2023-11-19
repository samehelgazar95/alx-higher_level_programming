#!/usr/bin/python3
for i in range(122, 96, -1):
    curr = i
    if curr % 2 != 0:
        curr -= 32
    print("{}".format(chr(curr)), end="")
