#!/usr/bin/python3
 
class_to_json = __import__('8-class_to_json').class_to_json

class First:
    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[First] {} - {:d}".format(self.name, self.number)

class Second:
    score = 0

    def __init__(self, name, number = 4):
        self.__name = name
        self.number = number
        self.is_team_red = (self.number % 2) == 0

    def win(self):
        self.score += 1

    def lose(self):
        self.score -= 1

    def __str__(self):
        return "[Second] {} - {:d} => {:d}".format(self.__name, self.number, self.score)
    
m = First("John")
m.number = 89
print(type(m))
print(m)
print(m.__dict__)

print("-------------------------------")

mj = class_to_json(m)
print(type(mj))
print(mj)

print("-------------------------------")
print("-------------------------------")

m = Second("Sameh")
m.win()
m.win()
print(type(m))
print(m)
print(m.__dict__)

print("-------------------------------")    

mj = class_to_json(m)
print(type(mj))
print(mj)
