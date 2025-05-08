#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
message = "Last digit of"
last_digit = number % 10 if number >= 0 else -(-number % 10)
if last_digit > 5:
    print(f"{message} {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"{message} {number} is {last_digit} and is 0")
elif last_digit < 6 and last_digit != 0:
    print(f"{message} {number} is {last_digit} and is less than 6 and not 0")
