#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 5:
    print("Last Digit of {} is greater than 5".format(number))
elif number == 0:
    print("Last Digit of {} is 0".format(number))
else:
    print("Last Digit of {} is less than 6 and not 0".format(number))
