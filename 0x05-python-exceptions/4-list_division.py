#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = 0
    new_list = []
    while i < list_length:
        try:
            if type(my_list_1[i]) not in [int, float] or type(my_list_2[i]) not in [int, float]:
                raise TypeError
            new_list.append(my_list_1[i] / my_list_2[i])
            i += 1
        except TypeError:
            i += 1
            new_list.append(0)
            print("wrong type")
        except ZeroDivisionError:
            i += 1
            new_list.append(0)
            print("division by 0")
        except IndexError:
            i += 1
            new_list.append(0)
            print("out of range")
        finally:
            pass
    return new_list
