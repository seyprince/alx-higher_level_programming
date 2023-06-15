#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
v = abs(number) % 10
if number < 0:
    v = -v
if v > 5:
    print(f"Last digit of {number} is {v} and is greater than 5")
elif v == 0:
    print(f"Last digit of {number} is {v} and is 0")
else:
    print(f"Last digit of {number} is {v} and is less than 6 and not 0")
