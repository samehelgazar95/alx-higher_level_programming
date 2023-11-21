#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    curr = None

    for i in range(list_length):
        try:
            curr = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            curr = 0
            print("division by 0")
        except (ValueError, TypeError):
            curr = 0
            print("wrong type")
        except IndexError:
            curr = 0
            print("out of range")
        finally:
            res.append(curr)

    return res
