#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 if number > 0 else (-number) % 10
if number < 0:
    last_digit *= -1
if last_digit == 0:
    print(f"Last digit of {number:d} is {last_digit:d} and is 0", end='\n')
elif last_digit > 5:
    print(f"Last digit of {number:d} is {last_digit:d} and is "
          "greater than 5", end='\n')
elif last_digit < 5:
    print(f"Last digit of {number:d} is {last_digit:d} "
          "and is less than 6 and not 0", end='\n')
