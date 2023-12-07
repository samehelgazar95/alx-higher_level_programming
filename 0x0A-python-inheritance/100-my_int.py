#!/usr/bin/python3


class MyInt(int):
    """Int Rebel Child Class"""

    def __init__(self, num):
        self.num = num

    def __eq__(self, other):
        if self.num == other:
            return False
        else:
            return True

    def __ne__(self, other):
        if self.num == other:
            return True
        else:
            return False
