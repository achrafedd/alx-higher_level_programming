#!/usr/bin/python3

def fizzbuzz():
    numbers = range(1, 101)
    for n in numbers:
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz", end=' ')
        elif n % 5 == 0:
            print("Buzz", end=' ')
        elif n % 3 == 0:
            print("Fizz", end=' ')
        else:
            print(f"{n}", end=' ')
